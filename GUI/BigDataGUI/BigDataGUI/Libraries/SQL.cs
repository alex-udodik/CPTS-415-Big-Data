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

        public string executeSearch(string word)
        {
            string wordLowercase = word.ToLower();
            int size = tableNames.Length;

            StringBuilder builder = new StringBuilder();

            foreach (string table in tableNames)
            {
                builder.Append("SELECT name FROM " + table + " ");
                builder.Append("WHERE lower(name) like '%" + word + "%' ");

                if (size > 1)
                {
                    builder.Append("UNION ALL ");
                }

                size--;
            }

            return builder.ToString();
        }
    }
}
