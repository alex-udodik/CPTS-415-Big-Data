using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;

namespace BigDataGUI.Libraries
{
	public class XMLHandler
	{
		private List<XMLItem> ownedContent; // list of owned content info
		private string currentFile = string.Empty; // current file name

		// constructor
		public XMLHandler()
		{
			this.ownedContent = new List<XMLItem>();
		}

		// Method for Updating an XML document
		public XmlDocument UpdateXML(XmlDocument doc)
		{
			XmlNode rootNode = doc.CreateElement("OwnedContent");

			// loop through owned Content list to create nodes for all content owned
			for (int i = 0; i < this.ownedContent.Count; i++)
			{
				XmlNode currentContent = doc.CreateElement("Content");

				// create Node for the current content key and append to the Content
				XmlNode currentKey = doc.CreateElement("Key");
				currentKey.InnerText = this.ownedContent[i].ID();
				currentContent.AppendChild(currentKey);

				// create Node for the name of content and append to the Content
				XmlNode currentName = doc.CreateElement("Name");
				currentName.InnerText = this.ownedContent[i].Name();
				currentContent.AppendChild(currentName);

				// create Node for the type of content and append to the Content
				XmlNode currentType = doc.CreateElement("Type");
				currentType.InnerText = this.ownedContent[i].Type();
				currentContent.AppendChild(currentType);

				// append to root
				rootNode.AppendChild(currentContent);
			}

			// append root to doc
			doc.AppendChild(rootNode);
			return doc;
		}

		// Method for Saving an XML document
		public void SaveXML(string name)
		{
			this.currentFile = name;
			string fileName = "\\" + name + ".xml";
			string path = Directory.GetCurrentDirectory().Replace("bin\\Debug", "");
			path += fileName;
			XmlDocument doc = new XmlDocument();
			doc = this.UpdateXML(doc);
			if (!File.Exists(path))
			{
				var myFile = File.Create(path);
				myFile.Close();
			}
			doc.Save(path);
		}

		public void addToOwnedContent(XMLItem info)
		{
			bool exists = false;
			int i = 0;
			while (i < this.ownedContent.Count)
			{
				if (this.ownedContent[i].ID() == info.ID())
				{
					exists = true;
					break;
				}
				i++;
			}
			if (exists == false)
			{
				this.ownedContent.Add(info);
				SaveXML("ACNH_OwnedContent");
			}
		}

		public void removeFromOwnedContent(string key)
		{
			bool exists = false;
			int i = 0;
			while (i < this.ownedContent.Count)
			{
				if (this.ownedContent[i].ID() == key)
				{
					exists = true;
					break;
				}
				i++;
			}
			if (exists == true)
			{
				this.ownedContent.RemoveAt(i);
				SaveXML(currentFile);
			}
		}

		// Method for loading in a specific XML document
		public XmlDocument LoadXML(string name)
		{
			this.currentFile = name;
			string fileName = "\\" + name + ".xml";
			string path = Directory.GetCurrentDirectory().Replace("bin\\Debug", "");
			path += fileName;
			XmlDocument doc = new XmlDocument();
			if (File.Exists(path))
			{
				doc.Load(path);
				this.readXML(doc);
			}
			return doc;
		}

		// Method for reading the XML doc to update the owned content list
		public void readXML(XmlDocument doc)
		{
			List<XMLItem> loadedContentList = new List<XMLItem>(); // create new list
			XmlNodeList nodeList = doc.SelectNodes("/OwnedContent/Content"); // create XML node list filled with all the content nodes

			// in each content node takt the inner text of the key and add it to the loaded content list
			foreach (XmlNode node in nodeList)
			{
				loadedContentList.Add(new XMLItem(node["Key"].InnerText, node["Name"].InnerText, node["Type"].InnerText));
			}

			this.ownedContent = loadedContentList; // update the owned content list;
		}

		public List<XMLItem> getOwnedContent()
		{
			return this.ownedContent;
		}

		public bool checkIfOwned(string key)
		{
			bool exists = false;
			int i = 0;
			while (i < this.ownedContent.Count)
			{
				if (this.ownedContent[i].ID() == key)
				{
					exists = true;
					break;
				}
				i++;
			}
			return exists;
		}

		public Dictionary<string, List<string>> createContentDictionary(string[] tableNames, List<XMLItem> contentList)
		{

			Dictionary<string, List<string>> contentDictionary = new Dictionary<string, List<string>>();
			foreach (string type in tableNames)
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
	}
}