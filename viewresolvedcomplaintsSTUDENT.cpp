#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;
int main()
{
    string line;
    cout<<setw(40)<<"THE RESOLVED COMPLAINTS "<<endl;
    cout<<"======================================================"<<endl<<endl;
    fstream file;
    file.open("resolved.txt",ios::in);
    while(getline(file,line))
    {
      cout<<line<<endl<<endl;
    }
  return 0;
}