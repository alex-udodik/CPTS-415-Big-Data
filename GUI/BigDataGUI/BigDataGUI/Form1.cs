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
            int rowIndex = dataGridViewSearchResultsLeft.CurrentCell.RowIndex;
            string id = searchResults.Rows[rowIndex][1].ToString();
            Console.WriteLine();
        }
    }
}
