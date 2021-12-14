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
        private StatsHandler statsHandler;
        private Dictionary<string, List<string>> contentDictionary;

        string[] tableNames = { "all", "accessories", "achievements", "art", "bags", "bottoms", "construction", "dressup", "fencing", "fish", "floors","fossils", "headwear",
                                            "housewares", "insects", "miscellaneous", "music", "other", "photos", "posters", "reactions", "recipes", "rugs", "shoes",
                                            "socks", "tools", "tops", "umbrellas", "villagers", "wallmounted", "wallpaper"};

        public Form1()
        {
            InitializeComponent();
            xmlHandler.LoadXML("ACNH_OwnedContent");
            this.statsHandler = new StatsHandler(this.tableNames);
            this.contentDictionary = this.xmlHandler.createContentDictionary(this.tableNames, this.xmlHandler.getOwnedContent());
            fillComboBox();
        }

        // method that handles performs a search after enter is pressed in the text box
        private void textBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Enter)
            {
                if(ownedBox.SelectedIndex == 0)
                {
                    this.performSearch();
                }
                else
                {
                    this.performOwnedUnownedSearch();
                }
                
            }
        }

        // method that performs the search
        private void performSearch()
        {
            Console.WriteLine("Enter pressed");
            string word = searchTextBox.Text.ToString();
            SQL sql = new SQL();
            StringBuilder query = new StringBuilder();

            // none selected
            if (comboBox1.SelectedIndex == 0 && comboBoxSearch.SelectedIndex == 0)
            {
                query.Append(sql.executeSearch(word));
            }

            //category only selected
            else if (comboBox1.SelectedIndex == 0 && comboBoxSearch.SelectedIndex != 0)
            {
                string category = comboBoxSearch.SelectedItem.ToString();
                query.Append(sql.GetQueryForFilterByCategorySearch(word, category));
            }

            //color only selected
            else if (comboBox1.SelectedIndex != 0 && comboBoxSearch.SelectedIndex == 0)
            {
                query.Append(sql.searchColor(comboBox1.Text.ToString(), word));
            }

            //both are selected
            else
            {
                string category = comboBoxSearch.SelectedItem.ToString();
                string color = comboBox1.SelectedItem.ToString();

                query.Append(sql.searchColorAndCategory(color, word, category));
            }

            DataTable original_table = sql.execute(query.ToString());
            DataTable modified_table = original_table.Copy();
            searchResults = original_table.Copy();
            modified_table.Columns.Remove("UniqueEntryID");

            dataGridViewSearchResultsLeft.DataSource = modified_table;
            dataGridViewSearchResultsLeft.Columns[0].Width = 200;
        }

        // method that performs the search
        private void performOwnedUnownedSearch()
        {
            Console.WriteLine("Enter pressed");
            string word = searchTextBox.Text.ToString();
            SQL sql = new SQL();
            StringBuilder query = new StringBuilder();

            // none selected
            if (comboBox1.SelectedIndex == 0 && comboBoxSearch.SelectedIndex == 0)
            {
                query.Append(sql.executeSearch(word, this.contentDictionary, this.ownedNotOwned()));
            }

            //category only selected
            else if (comboBox1.SelectedIndex == 0 && comboBoxSearch.SelectedIndex != 0)
            {
                string category = comboBoxSearch.SelectedItem.ToString();
                query.Append(sql.GetQueryForFilterByCategorySearch(word, category, this.contentDictionary, this.ownedNotOwned()));
            }

            //color only selected
            else if (comboBox1.SelectedIndex != 0 && comboBoxSearch.SelectedIndex == 0)
            {
                query.Append(sql.searchColor(comboBox1.Text.ToString(), word, this.contentDictionary, this.ownedNotOwned()));
            }

            //both are selected
            else
            {
                string category = comboBoxSearch.SelectedItem.ToString();
                string color = comboBox1.SelectedItem.ToString();

                query.Append(sql.searchColorAndCategory(color, word, category, this.contentDictionary, this.ownedNotOwned()));
            }

            DataTable original_table = sql.execute(query.ToString());
            DataTable modified_table = original_table.Copy();
            searchResults = original_table.Copy();
            modified_table.Columns.Remove("UniqueEntryID");

            dataGridViewSearchResultsLeft.DataSource = modified_table;
            dataGridViewSearchResultsLeft.Columns[0].Width = 200;
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

        // method to add to owned content
        private void button1_Click(object sender, EventArgs e)
        {
            this.xmlHandler.addToOwnedContent(createInfoForXML());
            this.contentDictionary = this.xmlHandler.createContentDictionary(this.tableNames, this.xmlHandler.getOwnedContent());
            dataGridViewSearchResultsLeft_CellClick(dataGridViewItemDetails, null);
        }

        // method to check if item is owned
        private bool checkIfOwned(string key)
        {
            return xmlHandler.checkIfOwned(key);
        }

        // method to remove from owned content
        private void button2_Click(object sender, EventArgs e)
        {
            this.xmlHandler.removeFromOwnedContent(createInfoForXML().ID());
            this.contentDictionary = this.xmlHandler.createContentDictionary(this.tableNames, this.xmlHandler.getOwnedContent());
            dataGridViewSearchResultsLeft_CellClick(dataGridViewItemDetails, null);
        }

        // method to perform search when color selection is changed
        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (ownedBox.SelectedIndex == 0)
            {
                this.performSearch();
            }
            else
            {
                this.performOwnedUnownedSearch();
            }
        }

       
        // method to create statistics
        private void button3_Click(object sender, EventArgs e)
        {
            this.statsHandler.createStats(xmlHandler.getOwnedContent());
        }

        // method to fill comboboxes
        private void fillComboBox()
        {
            foreach (string table in tableNames)
            {
                comboBoxSearch.Items.Add(table);
            }

            comboBox1.Items.Add("none");
            comboBox1.Items.Add("red");
            comboBox1.Items.Add("blue");
            comboBox1.Items.Add("green");
            comboBox1.Items.Add("yellow");
            comboBox1.Items.Add("black");
            comboBox1.Items.Add("white");
            comboBox1.Items.Add("colorful");

            ownedBox.Items.Add("both");
            ownedBox.Items.Add("owned");
            ownedBox.Items.Add("unowned");

            
            comboBoxSearch.SelectedIndex = 0;
            comboBox1.SelectedIndex = 0;
            ownedBox.SelectedIndex = 0;
        }

        // method to perform search when type selection is changed
        // if a specific type is selected that has color then enable combobox1
        // if a specific type is selected that does not have color then set color to none and disable combobox1
        private void comboBoxSearch_SelectedIndexChanged(object sender, EventArgs e)
        {
            string currentSelection = comboBoxSearch.GetItemText(comboBoxSearch.SelectedItem);
            
            if(currentSelection != "all")
            {
                SQL sql = new SQL();

                DataTable currentTable = sql.execute("select * from " + currentSelection);

                bool colorExists = checkIfColorExists(currentTable);

                if (colorExists)
                {
                    comboBox1.Enabled = true;
                }
                else
                {
                    comboBox1.SelectedIndex = 0;
                    comboBox1.Enabled = false;
                }
            } 
            else
            {
                comboBox1.SelectedIndex = 0;
                comboBox1.Enabled = true;
            }
            if (ownedBox.SelectedIndex == 0)
            {
                this.performSearch();
            }
            else
            {
                this.performOwnedUnownedSearch();
            }
        }

        // method to check if color exists in the table
        private bool checkIfColorExists(DataTable table)
        {
            bool colorExists = false;

            foreach (DataColumn column in table.Columns)
            {
                string columnName = column.ColumnName;

                if (columnName.Contains("color"))
                {
                    colorExists = true;
                }
            }
            return colorExists;
        }

        private bool ownedNotOwned()
        {
            if (this.ownedBox.SelectedIndex == 1)
            {
                return true;
            }
            return false;
        }

        private void ownedBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (ownedBox.SelectedIndex == 0)
            {
                this.performSearch();
            }
            else
            {
                this.performOwnedUnownedSearch();
            }
        }
    }
}
