using Npgsql;
using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BigDataGUI.Libraries
{
    public class SQL
    {
        private const string CONNECTION_STRING = "Host = localhost; Port = 5432; Username = postgres; Database = 415BigData; password = password";

        private string[] tableNames = { "accessories", "achievements", "art", "bags", "bottoms", "construction", "dressup", "fencing", "fish", "floors", "headwear",
                                            "housewares", "insects", "miscellaneous", "music", "other", "photos", "posters", "reactions", "recipes", "rugs", "shoes",
                                            "socks", "tools", "tops", "umbrellas", "villagers", "wallmounted", "wallpaper"};


        //this function takes in a SQL query in the form of a string and will return a DataTable with the results
        public DataTable execute(string query)
        {
           
            using (var connection = new NpgsqlConnection(CONNECTION_STRING))
            {
                try
                {
                    connection.Open();
                    using (var cmd = new NpgsqlCommand(query, connection))
                    {
                        try
                        {
                            DataTable dt = new DataTable();
                            NpgsqlDataAdapter da = new NpgsqlDataAdapter(cmd);
                            da.Fill(dt);
                            return dt;
                        }
                        catch (NpgsqlException e)
                        {
                            Console.WriteLine(e.Message.ToString());
                            string errorMessage = "SQL Error: " + e.Message.ToString() + "\n Failing Query: " + query;
                            MessageBox.Show(errorMessage, "SQL Error");
                            
                            return null;
                        }
                    }
                }

                catch (Exception e)
                {
                    Console.WriteLine("Exception: " + e.ToString());
                    return null;
                }
            }
        }


        // this function takes in a word to be searched and creates a
        // SQL query that will search all tables for that word
        public string executeSearch(string word)
        {
            string wordLowercase = word.ToLower();

            //this is used for making sure the last part of the query does not contain 'UNION ALL'
            int size = tableNames.Length;

            StringBuilder builder = new StringBuilder();

            
            foreach (string table in tableNames)
            {
                builder.Append("SELECT distinct name, UniqueEntryID FROM " + table + " ");
                builder.Append("WHERE lower(name) like '%" + wordLowercase + "%' ");

                if (size > 1)
                {
                    builder.Append("UNION ALL ");
                }

                size--;
            }

            
            return builder.ToString();
        }

        public string getItemInfo(string UniqueEntryID)
        {

            return "";
        }

        // creats a sql statement to search for a kind of color
        //
        public string searchColor(string color, string word)
        {
            string[] colorTable = {"accessories", "art", "bags", "bottoms", "dressup","fish","floors","fossils","headwear","housewares","insects","miscellaneous",
              "music","other","photos","posters","rugs","shoes","socks","tools","tops","umbrellas","villagers","wallmounted","wallpaper" };

            int size = colorTable.Length;

            StringBuilder builder = new StringBuilder();

            if (word == "")
            {
                foreach (string table in colorTable)
                {
                    builder.Append("SELECT distinct name, UniqueEntryID FROM " + table + " ");
                    builder.Append("WHERE lower(color1) like '%" + color + "%' or lower(color2) like '%" + color + "%' ");

                    if (size > 1)
                    {
                        builder.Append("UNION ALL ");
                    }

                    size--;
                }

            }
            else
            {

                foreach (string table in colorTable)
                {

                    builder.Append("SELECT distinct name, UniqueEntryID FROM " + table + " ");
                    builder.Append("WHERE lower(name) like '%" + word + "%' and ( lower(color1) like '%" + color + "%' or lower(color2) like '%" + color + "%') ");

                    if (size > 1)
                    {
                        builder.Append("UNION ALL ");
                    }

                    size--;
                }
            }

            return builder.ToString();
        }
    }
}

