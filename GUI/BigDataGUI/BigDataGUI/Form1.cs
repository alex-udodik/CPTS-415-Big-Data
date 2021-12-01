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

                DataTable table = sql.execute(query);
                dataGridViewSearchResultsLeft.DataSource = table;
            }
            else
            {
                Console.WriteLine("Other button pressed");
            }
        }
    }
}
