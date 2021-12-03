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

        public Form1()
        {
            InitializeComponent();
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

            int rowIndex = dataGridViewSearchResultsLeft.CurrentCell.RowIndex;
            string id = searchResults.Rows[rowIndex][1].ToString();

            SQL sql = new SQL();

            //this table will hold the tableName for the ID. We need the table for a simple lookup
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

            //once the table is built, pop it into the datagridview box.
            dataGridViewItemDetails.DataSource = processedItemDetails;


            //this is old code for dynamically adding labels to a groupbox. It works cool but if there text of an attribute value
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
            Console.WriteLine();
        }
    }
}
