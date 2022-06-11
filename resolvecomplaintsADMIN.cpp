#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include<ios>
#include<limits>
using namespace std;
void resolve_complaints()
{

    fstream file1, file2,file3;
    string line;
    file1.open("complaints.txt",  ios::in);
    file2.open("unresolved_complaint.txt", ios::out);
    file3.open("resolved.txt",ios::app);
    cout<<endl<<setw(30)<<"COMPLAINTS"<<endl<<endl;
   /* while (file1.eof() == 0)
    {
        getline(file1, line);
        cout << line << endl;
    }
    cout << endl
         << "===========================================================" << endl;
    line.clear(); */
    string numstr,yellow;
    int num;
    cout << "Enter Complaint Number : ";
    cin >> num;
    numstr = to_string(num);
    int a = numstr.size();
    while ( file1.eof()==0)
    {
        getline(file1,line);
        yellow = line.substr(0,a);
        if(yellow!=numstr)
        {
            file2<<line<<endl;
        }
        else
        {
            file3<<line<<endl;
        }
    }
    file1.close();
    file2.close();
    file3.close();
    remove("complaints.txt");
    rename("unresolved_complaint.txt","complaints.txt");
   
    cout << "COMPLAINT SUCCESSFULLY RESOLVED AND UPDATED !!!" << endl;
}
void log_of_resolved_complaints()
{
    ifstream file;
    string line;
    file.open("resolved.txt", ios::in);
    cout << setw(30) << "LOG OF RESOLVED COMPLAINTS " << endl
         << endl;
    cout << "==================================================================" << endl
         << endl;
    while (file.eof() == 0)
    {
        getline(file, line);
        cout << line << endl
             << endl;
    }
}
int main()
{
    int n;
    cout << setw(45) << "WELCOME TO RESOLVE COMPLAINT SECTION " << endl;
    cout << "=============================================================" << endl
         << endl;
    cout << setw(30) << "MENU" << endl
         << endl;
    cout << "1 : To resolve a complaint " << endl
         << endl
         << "2 : To view already resolved complaints " << endl
         << endl;
    cout << "Enter an appropriate Number : ";
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(),'\n');
    switch (n)
    {
    case 1:
    {
        resolve_complaints();
        break;
    }
    case 2:
    {
        log_of_resolved_complaints();
        break;
    }
    default:
        cout << "Invalid Input" << endl;
    }
    return 0;
}