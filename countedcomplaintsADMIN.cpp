#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int count = 001 ;
    string line,app_line,yellow;
    fstream file1,file2;
    file1.open("complaint.txt",ios::in);
    file2.open("complaints.txt",ios::app|ios::out);
    while(getline(file1,line))
    {
        yellow = to_string(count);
        app_line = yellow + "     " + line;
        file2<<app_line<<endl;
        count++;
        yellow.clear();
    }

    return 0;

}