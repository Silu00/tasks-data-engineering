import sys;sys.stdout.reconfigure(newline='\n')
HubertSilukTest = r"""public class Solution {

    public static void main(String[] args) {

    String HubertSilukTest = %c%s%c;

    String py = "";
    py += "import sys;sys.stdout.reconfigure(newline='\\n')\n";
    py += "HubertSilukTest = r\"\"\"";
    py += HubertSilukTest;
    py += "\"\"\"\n";
    py += "print(HubertSilukTest %% (34, HubertSilukTest.replace('\\\\', '\\\\\\\\').replace(chr(10), \"\\\\n\").replace(chr(34), \"\\\\\\\"\"), 34), end=\"\")";

    String jsString = py
        .replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace("\"", "\\\"");

    System.out.print("const code = \"");
    System.out.print(jsString);
    System.out.print("\";\n");
    System.out.print("process.stdout.write(code);\n");

    }

}"""
print(HubertSilukTest % (34, HubertSilukTest.replace('\\', '\\\\').replace(chr(10), "\\n").replace(chr(34), "\\\""), 34), end="")
