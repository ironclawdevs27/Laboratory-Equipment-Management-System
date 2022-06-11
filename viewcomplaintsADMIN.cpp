#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;
void particular_string_to_file_copy(void)
{
    string LabNo,line;
    cout<<endl<<"Enter the Lab Number : ";
    cin>>LabNo;
    //check lab no
    fstream myfile;
    myfile.open("complaint.txt",ios::app|ios::in);
    cout<<endl<<setw(40)<<" COMPLAINTS OF LAB "<<LabNo<<endl;
    cout<<"=================================================================="<<endl<<endl;
    while(myfile.eof()==0)
    {
    getline(myfile,line);
    int a = line.find(LabNo);
    if(a==0)
    {
        cout<<line<<endl<<endl;
    }
    }
    cout<<"===================================================================="<<endl;
}
void view_complaints()
{
    string line;
    ifstream file1;
    file1.open("complaint.txt",ios::in);
    while(file1.eof()==0)
    {
        getline(file1,line);
        cout<<line<<endl<<endl;
    }
}
int main()
{
    cout<<setw(30)<<"WELCOME TO COMPLAINT SECTION "<<endl<<endl;
    cout<<setw(20)<<"MENU"<<endl<<endl;
    cout<<"1 : To check the complaints of One Particular Lab"<<endl<<endl
        <<"2 : To check all the complaints "<<endl<<endl;
    int n;
    cout<<"Enter the appropiate number : ";
    cin>>n;
    switch(n)
    {
        case 1:
        {
            particular_string_to_file_copy();
          break;
        }
        case 2:
        {
             view_complaints();
            break;
        }
        default:
        cout<<"Inavlid Input "<<endl;
    }
   
    return 0;
}