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

		public StatsHandler(List<XMLItem> ownedContent)
		{
			this.typeList = createTypeList(ownedContent);
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
	
		private List<string> createTypeList(List<XMLItem> contentList)
		{
			List<string> typeList = new List<string>();

			foreach (XMLItem item in contentList)
			{
				if(!typeList.Contains(item.Type()))
				{
					typeList.Add(item.Type());
				}
			}

			return typeList;
		}

		private Dictionary<string, List<string>> createContentDictionary(List<XMLItem> contentList)
		{
			Dictionary<string, List<string>> contentDictionary = new Dictionary<string, List<string>>();
	
			// check each XMLItem in the content list and build a dictionary of items of team
			foreach (XMLItem item in contentList)
			{
				string currentType = item.Type();
				string currentKey = item.ID();

				if (contentDictionary.ContainsKey(currentType))
				{
					contentDictionary[currentType].Add(currentKey);
				}
				else
				{
					contentDictionary.Add(currentType, new List<String>());
					contentDictionary[currentType].Add(currentKey);
				}
			}
	
			return contentDictionary;
		}
	
		private string writePercentOwned(Dictionary<string, List<string>> contentDictionary)
		{
			string percentOwned = string.Empty;
			percentOwned += "Percent Owned of Each Content Type Owned\n \n";
	
			typeList.Sort();
			foreach (string type in typeList)
			{
				double currentCount = contentDictionary[type].Count;
				double totalCount = getTotalFromTable(type);
				double percent = (currentCount * 100) / (totalCount * 100) ;
	
				percentOwned += type + "\n";
				percentOwned += "   " + currentCount + "/" + totalCount + " owned\n";
				percentOwned += "   " + percent + "% completion\n\n";
			}
			return percentOwned;
		}

		private int getTotalFromTable(string type)
		{
			SQL sql = new SQL();
			DataTable typeTable = sql.execute("select * from " + type);
			return typeTable.Rows.Count;
		}
	}
}
