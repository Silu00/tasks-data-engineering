import sys;sys.stdout.reconfigure(newline='\n')
HubertSilukTest = r"""public class Solution {
    public static void main(String[] args) {
    String HubertSilukTest = %c%s%c;
    System.out.print("import sys;sys.stdout.reconfigure(newline='\\n')\n");
    System.out.print("HubertSilukTest = r\"\"\"");
    System.out.print(HubertSilukTest);
    System.out.print("\"\"\"\n");
    System.out.print("print(HubertSilukTest %% (34, HubertSilukTest.replace('\\\\', '\\\\\\\\').replace(chr(10), \"\\\\n\").replace(chr(34), \"\\\\\\\"\"), 34), end=\"\")");
    }
}"""
print(HubertSilukTest % (34, HubertSilukTest.replace('\\', '\\\\').replace(chr(10), "\\n").replace(chr(34), "\\\""), 34), end="")
