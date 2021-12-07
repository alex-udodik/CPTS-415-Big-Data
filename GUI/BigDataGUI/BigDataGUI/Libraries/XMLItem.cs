using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BigDataGUI.Libraries
{
    public class XMLItem
    {
        private string id;
        private string name;
        private string type;

        public XMLItem(string id, string name, string type)
        {
            this.id = id;
            this.name = name;
            this.type = type;
        }

        public string ID()
        {
            return this.id;
        }

        public string Name()
        {
            return this.name;
        }

        public string Type()
        {
            return this.type;
        }
    }
}
