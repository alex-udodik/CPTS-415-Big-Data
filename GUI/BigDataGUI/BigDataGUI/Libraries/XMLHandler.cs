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
		private List<string> ownedContent; // list of keys for the content owned
		private string currentFile = string.Empty; // current file name

		// constructor
		public XMLHandler()
		{
			this.ownedContent = new List<string>();
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
				currentKey.InnerText = this.ownedContent[i];
				currentContent.AppendChild(currentKey);

				// create Node for the type of content and append to the Content
				XmlNode currentName = doc.CreateElement("Name");
				currentName.InnerText = ("THIS IS WIP");
				currentContent.AppendChild(currentName);

				// create Node for the type of content and append to the Content
				XmlNode currentType = doc.CreateElement("Type");
				currentType.InnerText = ("THIS IS WI");
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
			string path = Directory.GetCurrentDirectory() + fileName;
			XmlDocument doc = new XmlDocument();
			doc = this.UpdateXML(doc);
			if (!File.Exists(path))
			{
				var myFile = File.Create(path);
				myFile.Close();
			}
			doc.Save(path);
		}

		public void addToOwnedContent(string key)
		{
			bool exists = false;
			int i = 0;
			while(i < this.ownedContent.Count || exists == false)
			{
				if (this.ownedContent[i] == key)
				{
					exists = true;
				}
				i++;
			}
			if (exists = false)
			{
				this.ownedContent.Add(key);
				this.ownedContent.Sort();
				SaveXML(currentFile);
			}
		}

		public void removeFromOwnedContent(string key)
		{
			bool exists = false;
			int i = 0;
			while(i < this.ownedContent.Count || exists == false)
			{
				if (this.ownedContent[i] == key)
				{
					exists = true;
				}
				i++;
			}
			if (exists = true)
			{
				this.ownedContent.RemoveAt(i - 1);
				this.ownedContent.Sort();
				SaveXML(currentFile);
			}
		}

		// Method for loading in a specific XML document
		public XmlDocument LoadXML(string name)
		{
			this.currentFile = name;
			string fileName = "\\" + name + ".xml";
			string path = Directory.GetCurrentDirectory() + fileName;
			XmlDocument doc = new XmlDocument();
			doc.Load(path);
			this.readXML(doc);
			return doc;
		}

		// Method for reading the XML doc to update the owned content list
		public void readXML(XmlDocument doc)
		{
			List<string> loadedContentList = new List<string>(); // create new list
			XmlNodeList nodeList = doc.SelectNodes("/OwnedContent/Content"); // create XML node list filled with all the content nodes

			// in each content node takt the inner text of the key and add it to the loaded content list
			foreach (XmlNode node in nodeList)
			{
				loadedContentList.Add(node["Key"].InnerText);
			}

			loadedContentList.Sort(); // sort list
			this.ownedContent = loadedContentList; // update the owned content list;
		}
	}
}
