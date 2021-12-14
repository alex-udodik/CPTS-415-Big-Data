using System;
using System.Collections.Generic;
using System.Data;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BigDataGUI.Libraries
{
	public class StatsHandler
	{
		private List<string> typeList = new List<string>();
		private string stats;

		public StatsHandler(string[] tableNames)
		{
			this.typeList = createTypeList(tableNames);
			this.stats = string.Empty;
		}

		public void createStats(List<XMLItem> contentList)
		{
			Dictionary<string, List<string>> contentDictionary = createContentDictionary(contentList);
			this.stats += writePercentOwned(contentDictionary);

			string fileName = "\\stats.txt";
			string path = Directory.GetCurrentDirectory().Replace("bin\\Debug", "");
			path += fileName;

			// delete current stats file if it already exists
			if (File.Exists(path))
			{
				File.Delete(path);
			}

			using (FileStream fs = File.Create(path))
			{
				// Add some text to file    
				Byte[] stats = new UTF8Encoding(true).GetBytes(this.stats);
				fs.Write(stats, 0, stats.Length);
			}
		}

		private List<string> createTypeList(string[] tableNames)
		{
			List<string> typeList = new List<string>();

			foreach (string type in tableNames)
			{
				typeList.Add(type);
			}
			typeList.Remove(tableNames[0]);
			typeList.Add(tableNames[0]);
			return typeList;
		}

		private Dictionary<string, List<string>> createContentDictionary(List<XMLItem> contentList)
		{

			Dictionary<string, List<string>> contentDictionary = new Dictionary<string, List<string>>();

			foreach(string type in this.typeList)
			{
				contentDictionary.Add(type, new List<String>());
			}

			// check each XMLItem in the content list and build a dictionary of items of team
			foreach (XMLItem item in contentList)
			{
				contentDictionary["all"].Add(item.ID());
				contentDictionary[item.Type().ToLower()].Add(item.ID());
			}

			return contentDictionary;
		}

		private string writePercentOwned(Dictionary<string, List<string>> contentDictionary)
		{
			string percentOwned = string.Empty;
			percentOwned += "Percent Owned of Each Content Type Owned\n \n";
			foreach (string type in typeList)
			{
				double currentCount = contentDictionary[type].Count;
				double totalCount = getTotalFromTable(type);
				double percent = (currentCount * 100) / (totalCount * 100);

				percentOwned += type + "\n";
				percentOwned += "   " + currentCount + "/" + totalCount + " owned\n";
				percentOwned += "   " + percent + "% completion\n\n";
			}
			return percentOwned;
		}

		private int getTotalFromTable(string type)
		{
			SQL sql = new SQL();
			DataTable typeTable;
			if (type == "all")
			{
				typeTable = sql.execute("select Count(uniqueentryid) from Mapping");
			}
			else
			{
				typeTable = sql.execute("select Count(uniqueentryid) from " + type);
			}

			return Int32.Parse(typeTable.Rows[0][0].ToString());
		}
	}
}