using BigDataGUI.Libraries;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BigDataGUI
{
    public partial class Form1 : Form
    {
        private DataTable searchResults;
        private XMLHandler xmlHandler = new XMLHandler();
        public Form1()
        {
            InitializeComponent();
            xmlHandler.LoadXML("ACNH_Stats");
        }

        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Enter)
            {
                Console.WriteLine("Enter pressed");

                string word = searchTextBox.Text.ToString();
                SQL sql = new SQL();
                string query = sql.executeSearch(word);

                DataTable original_table = sql.execute(query);
                DataTable modified_table = original_table.Copy();
                searchResults = original_table.Copy();
                modified_table.Columns.Remove("UniqueEntryID");

                dataGridViewSearchResultsLeft.DataSource = modified_table;
                dataGridViewSearchResultsLeft.Columns[0].Width = 200;
            }
            else
            {
                Console.WriteLine("Other button pressed");
            }
        }


        // if there are search results and a cell is clicked, this will inititate.
        private void dataGridViewSearchResultsLeft_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            //groupBoxItemDetails.Controls.Clear();

            //the rowindex of the cell that was clicked.
            int rowIndex = dataGridViewSearchResultsLeft.CurrentCell.RowIndex;

            //the id of the item. The grid doesnt show it, but searchResults does (it's defined at the top and used on line 35)
            string id = searchResults.Rows[rowIndex][1].ToString();

            SQL sql = new SQL();

            //this table will hold the tableName for the ID. We need the table name for a simple lookup. The mapping table in the schema is handy for this.
            DataTable mappedPair = sql.execute("select tableName from Mapping where uniqueentryid = '" + id + "'");
            string tableName = mappedPair.Rows[0][0].ToString();

            //item details are now in this datatable object. It's just 1 row with all the columns.
            DataTable itemDetails = sql.execute("select * from " + tableName + " where uniqueentryid = '" + id + "'");

            //the amount of attributes an item has.
            int columns = itemDetails.Columns.Count;

            //creating a new datatable. There will be 2 columns. Column 1: Attribute_Name | Column 2: Attribute_value.
            //The amount of rows is based on how many attributes of the item there are.
            DataTable processedItemDetails = new DataTable();
            processedItemDetails.Columns.Add("Attribute", typeof(string));
            processedItemDetails.Columns[0].ColumnName = "Attribute";

            processedItemDetails.Columns.Add("Value", typeof(string));
            processedItemDetails.Columns[1].ColumnName = "Value";

            //create the rows and put them into the new table
            for (int i = 0; i < columns; i++)
            {
                var cellValue = itemDetails.Rows[0][i];

                DataRow row = processedItemDetails.NewRow();
                row[0] = itemDetails.Columns[i].ColumnName.ToString();
                row[1] = cellValue.ToString();
                processedItemDetails.Rows.Add(row);
            }
            
            DataRow owned = processedItemDetails.NewRow();
            owned[0] = "Owned";
            if(!checkIfOwned(id))
            {
                owned[1] = "No";
            } 
            else
            {
                owned[1] = "Yes";
            }
            processedItemDetails.Rows.Add(owned);


            //once the table is built, pop it into the datagridview box.
            dataGridViewItemDetails.DataSource = processedItemDetails;
            dataGridViewItemDetails.Columns[0].Width = 150;
            dataGridViewItemDetails.Columns[1].Width = 350;

            //this is old code for dynamically adding labels to a groupbox. It works cool but if the text of an attribute value
            //is too long (description), it will push labels off the group box. There is no scroll bar. Idk how to make it
            // 
            /*
            int y = 20;
            for (int i = 0; i < columns; i++)
            {
                var cellValue = itemDetails.Rows[0][i];

                //create a new label in the form of {attribute_name: attribute_value} and add to groupbox
                Label label = new Label { Text = itemDetails.Columns[i].ColumnName + ": " + cellValue.ToString() };
                label.Location = new Point(20, y);
                label.Font = new Font("Microsoft Sans Serif", 11);

                //groupBoxItemDetails.Controls.Add(label);

                y += 25;
            }
            */

            string name = "";

            //try and find the name value in item details
            foreach (DataRow row in processedItemDetails.Rows)
            {
                if (row["Attribute"].ToString().ToLower() == "name")
                {
                    name = row["Value"].ToString();
                }
            }

            //parse the name to be fit into a url
            string parseName = convertNameForURL_LookUp(name);

            //construct the link with the newly parsed name
            string wikiLink = getUrlFromItemName(parseName);

            //set the linklabel text to the link
            linkLabelWiki.Text = wikiLink;
            linkLabelWiki.LinkArea = new LinkArea(0, wikiLink.Length);
        }


        //this parses a name so it can be fit into a url. basically capitilizes the first
        //char in each word and makes empty spaces underscores.
        private string convertNameForURL_LookUp(string name)
        {
            StringBuilder builder = new StringBuilder();
            bool beginning = true;
            string previous = name[0].ToString();

            foreach (char c in name)
            {
                string character = c.ToString();

                if (beginning == true)
                {
                    builder.Append(character.ToUpper());
                    beginning = false;
                }
                else
                {
                    if (character == " ")
                    {
                        builder.Append("_");
                    }
                    else if (previous == "-" || previous == " ")
                    {
                        builder.Append(character.ToUpper());
                    }
                    
                    else
                    {
                        builder.Append(character);
                    }
                }

                previous = character;
            }

            return builder.ToString();
        }

        //contructs a url from a parsed name
        private string getUrlFromItemName(string parsedName)
        {
            StringBuilder builder = new StringBuilder();
            builder.Append("https://nookipedia.com/wiki/Item:" + parsedName + "_(New_Horizons)");
            //builder.Append("https://nookipedia.com/wiki/" + parsedName);
            return builder.ToString();
        }

        //when link label is clicked on, open in browser.
        private void linkLabelWiki_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            if (linkLabelWiki.Text.ToString().Length > 0)
            {
                System.Diagnostics.Process.Start(linkLabelWiki.Text.ToString());
            }
            
        }

        // info for the XMLHandler
        private XMLItem createInfoForXML()
        {
            //the rowindex of the cell that was clicked.
            int rowIndex = dataGridViewSearchResultsLeft.CurrentCell.RowIndex;

            //the id of the item. The grid doesnt show it, but searchResults does (it's defined at the top and used on line 35)
            string id = searchResults.Rows[rowIndex][1].ToString();

            // the name of the item.
            string name = searchResults.Rows[rowIndex][0].ToString();

            SQL sql = new SQL();

            //this table will hold the tableName for the ID.
            DataTable mappedPair = sql.execute("select tableName from Mapping where uniqueentryid = '" + id + "'");
            string tableName = mappedPair.Rows[0][0].ToString();

            XMLItem info = new XMLItem(id, name, tableName);

            return info;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            xmlHandler.addToOwnedContent(createInfoForXML());
            dataGridViewSearchResultsLeft_CellClick(dataGridViewItemDetails, null);
        }

        private bool checkIfOwned(string key)
        {
            return xmlHandler.checkIfOwned(key);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            xmlHandler.removeFromOwnedContent(createInfoForXML().ID());
            dataGridViewSearchResultsLeft_CellClick(dataGridViewItemDetails, null);
        }
    }
}
