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

        private string[] tableNames = { "accessories", "achievements", "art", "bags", "bottoms", "construction", "dressup", "fencing", "fish", "floors","fossils", "headwear",
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

        // this function takes in a word to be searched and creates a
        // SQL query that will search all tables for that word
        public string executeSearch(string word, Dictionary<string, List<string>> contentDictionary, bool owned)
        {
            string wordLowercase = word.ToLower();

            //this is used for making sure the last part of the query does not contain 'UNION ALL'
            int size = tableNames.Length;

            StringBuilder builder = new StringBuilder();

            if (!owned)
            {
                foreach (string table in tableNames)
                {
                    builder.Append("SELECT distinct name, UniqueEntryID FROM " + table + " ");
                    builder.Append("WHERE lower(name) like '%" + wordLowercase + "%' ");

                    foreach (string key in contentDictionary[table])
                    {
                        builder.Append("AND UniqueEntryID <> '" + key + "' ");
                    }

                    if (size > 1)
                    {
                        builder.Append("UNION ALL ");
                    }

                    size--;
                }
            }
            else
            {
                List<string> ownedList = ownedItemListGenerator(contentDictionary);
                size = ownedList.Count;
                foreach (string table in ownedList)
                {
                    builder.Append("SELECT distinct name, UniqueEntryID FROM " + table + " ");
                    builder.Append("WHERE lower(name) like '%" + wordLowercase + "%' ");

                    bool pastFirst = false;
                    int i = contentDictionary[table].Count;
                    foreach (string key in contentDictionary[table])
                    {
                        if(!pastFirst)
                        {
                            builder.Append("AND (");
                            pastFirst = true;
                        }
                        else
                        {
                            builder.Append("OR ");
                        }
                        builder.Append(" UniqueEntryID = '" + key + "' ");
                        i--;
                        if(i == 0)
                        {
                            builder.Append(")");
                        }
                    }

                    if (size > 1)
                    {
                        builder.Append("UNION ALL ");
                    }

                    size--;
                }
            }
            


            return builder.ToString();
        }

        public List<string> ownedItemListGenerator(Dictionary<string, List<string>> contentDictionary)
        {
            List<string> ownedList = new List<string>();
            foreach(string table in tableNames)
            {
                if(contentDictionary[table].Count > 0)
                {
                    ownedList.Add(table);
                }
            }
            
            return ownedList;
        }

        public List<string> ownedItemListGenerator(string[] otherTable, Dictionary<string, List<string>> contentDictionary)
        {
            List<string> ownedList = new List<string>();
            foreach (string table in otherTable)
            {
                if (contentDictionary[table].Count > 0)
                {
                    ownedList.Add(table);
                }
            }

            return ownedList;
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

        // creats a sql statement to search for a kind of color
        //
        public string searchColor(string color, string word, Dictionary<string, List<string>> contentDictionary, bool owned)
        {
            string[] colorTable = {"accessories", "art", "bags", "bottoms", "dressup","fish","floors","fossils","headwear","housewares","insects","miscellaneous",
              "music","other","photos","posters","rugs","shoes","socks","tools","tops","umbrellas","villagers","wallmounted","wallpaper" };

            int size = colorTable.Length;

            StringBuilder builder = new StringBuilder();


            if (!owned)
            {
                foreach (string table in colorTable)
                {
                    builder.Append("SELECT distinct name, UniqueEntryID FROM " + table + " ");
                    builder.Append("WHERE lower(name) like '%" + word + "%' and ( lower(color1) like '%" + color + "%' or lower(color2) like '%" + color + "%') ");

                    foreach (string key in contentDictionary[table])
                    {
                        builder.Append("AND UniqueEntryID <> '" + key + "' ");
                    }

                    if (size > 1)
                    {
                        builder.Append("UNION ALL ");
                    }

                    size--;
                }
            }
            else
            {
                List<string> ownedList = ownedItemListGenerator(colorTable, contentDictionary);
                size = ownedList.Count;
                foreach (string table in ownedList)
                {
                    builder.Append("SELECT distinct name, UniqueEntryID FROM " + table + " ");
                    builder.Append("WHERE lower(name) like '%" + word + "%' and ( lower(color1) like '%" + color + "%' or lower(color2) like '%" + color + "%') ");

                    bool pastFirst = false;
                    int i = contentDictionary[table].Count;
                    foreach (string key in contentDictionary[table])
                    {
                        if (!pastFirst)
                        {
                            builder.Append("AND (");
                            pastFirst = true;
                        }
                        else
                        {
                            builder.Append("OR ");
                        }
                        builder.Append(" UniqueEntryID = '" + key + "' ");
                        i--;
                        if (i == 0)
                        {
                            builder.Append(")");
                        }
                    }

                    if (size > 1)
                    {
                        builder.Append("UNION ALL ");
                    }

                    size--;
                }
            }

            return builder.ToString();
        }

        public string searchColorAndCategory(string color, string word, string category)
        {
            string[] colorTable = {"accessories", "art", "bags", "bottoms", "dressup","fish","floors","fossils","headwear","housewares","insects","miscellaneous",
              "music","other","photos","posters","rugs","shoes","socks","tools","tops","umbrellas","villagers","wallmounted","wallpaper" };


            StringBuilder builder = new StringBuilder();
            bool columnContainsColor = false;

            //does the table contain color column
            foreach(string table in colorTable)
            {
                if (table == category)
                {
                    columnContainsColor = true;
                }
            }

            //if columnContainsColor is true
            if (columnContainsColor)
            {
                //if word is empty
                if (word == "")
                {
                    builder.Append("SELECT distinct name, UniqueEntryID FROM " + category + " ");
                    builder.Append("WHERE lower(color1) like '%" + color + "%' or lower(color2) like '%" + color + "%' ");
                }

                //if not empty
                else
                {
                    builder.Append("SELECT distinct name, UniqueEntryID FROM " + category + " ");
                    builder.Append("WHERE lower(name) like '%" + word + "%' and ( lower(color1) like '%" + color + "%' or lower(color2) like '%" + color + "%') ");
                }
            }
            else
            {
                //return nothing
                builder.Append("SELECT distinct name, UniqueEntryID FROM " + category + " where name = '@@@@@@@-5000'");
            }
           

            return builder.ToString();
        }

        public string searchColorAndCategory(string color, string word, string category, Dictionary<string, List<string>> contentDictionary, bool owned)
        {
            string[] colorTable = {"accessories", "art", "bags", "bottoms", "dressup","fish","floors","fossils","headwear","housewares","insects","miscellaneous",
              "music","other","photos","posters","rugs","shoes","socks","tools","tops","umbrellas","villagers","wallmounted","wallpaper" };


            StringBuilder builder = new StringBuilder();
            bool columnContainsColor = false;


            //does the table contain color column
            foreach (string table in colorTable)
            {
                if (table == category)
                {
                    columnContainsColor = true;
                }
            }

            //if columnContainsColor is true
            if (columnContainsColor)
            {
                builder.Append("SELECT distinct name, UniqueEntryID FROM " + category + " ");
                builder.Append("WHERE lower(name) like '%" + word + "%' and ( lower(color1) like '%" + color + "%' or lower(color2) like '%" + color + "%') ");

                if (owned)
                {
                    bool pastFirst = false;
                    if (contentDictionary[category].Count > 0)
                    {
                        int i = contentDictionary[category].Count;
                        foreach (string key in contentDictionary[category])
                        {
                            if (!pastFirst)
                            {
                                builder.Append("AND (");
                                pastFirst = true;
                            }
                            else
                            {
                                builder.Append("OR ");
                            }
                            builder.Append(" UniqueEntryID = '" + key + "' ");
                            i--;
                            if (i == 0)
                            {
                                builder.Append(")");
                            }
                        }
                    }
                    else
                    {
                        builder.Append("AND UniqueEntryID = '-'");
                    }
                }

                else
                {
                    if (contentDictionary[category].Count > 0)
                    {
                        foreach (string key in contentDictionary[category])
                        {
                            builder.Append("AND UniqueEntryID <> '" + key + "' ");
                        }
                    }
                }
            }
            else
            {
                //return nothing
                builder.Append("SELECT distinct name, UniqueEntryID FROM " + category + " where name = '@@@@@@@-5000'");
            }


            return builder.ToString();
        }

        public string GetQueryForFilterByCategorySearch(string word, string table)
        {
            string wordLowercase = word.ToLower();

            string query = "SELECT distinct name, UniqueEntryID FROM " + table +
                " where lower(name) like '%" + wordLowercase + "%'";

            return query;
        }

        public string GetQueryForFilterByCategorySearch(string word, string table, Dictionary<string, List<string>> contentDictionary, bool owned)
        {
            string wordLowercase = word.ToLower();

            string query = "SELECT distinct name, UniqueEntryID FROM " + table +
                " where lower(name) like '%" + wordLowercase + "%'";

            if (owned)
            {
                bool pastFirst = false;
                if(contentDictionary[table].Count > 0)
                {
                    int i = contentDictionary[table].Count;
                    foreach (string key in contentDictionary[table])
                    {
                        if (!pastFirst)
                        {
                            query += "AND (";
                            pastFirst = true;
                        }
                        else
                        {
                            query += "OR ";
                        }
                        query += " UniqueEntryID = '" + key + "' ";
                        i--;
                        if (i == 0)
                        {
                            query += ")";
                        }
                    }
                }
                else
                {
                    query += "AND UniqueEntryID = '-'";
                }
            }
                
            else
            {
                if (contentDictionary[table].Count > 0)
                {
                    foreach (string key in contentDictionary[table])
                    {
                        query += "AND UniqueEntryID <> '" + key + "' ";
                    }
                }
            }

            return query;
        }
    }

   
}

