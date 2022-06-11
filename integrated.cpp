#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <string>
#include <ios>
#include <limits>
#include<map>
#include<iterator>
#include<algorithm>
#include<vector>
#include<list>
#include<iomanip>
using namespace std;
map<string,vector<list<string> > >sys;
map<string,vector<list<string> > >::iterator itr;
vector<list<string> >::iterator vtr;
list<string>::iterator j;
string stat[5];
string comp[5]={"Complete status","Mouse","Keyboard","Monitor","CPU"};

class system
{
protected:
    string sys_no;
    string comp_stat;
    string mouse_stat;
    string keyboard_stat;
    string monitor_stat;
    string cpu_stat;
    public:
    system()
    {
     sys_no="";
     comp_stat="";
     mouse_stat="";
     keyboard_stat="";
     monitor_stat="";
     cpu_stat="";

    }
    void address()
    {

    stat[0]=comp_stat;
    stat[1]=mouse_stat;
    stat[2]=keyboard_stat;
    stat[3]=monitor_stat;
    stat[4]=cpu_stat;
    }
    void address_back()
    {
    comp_stat=stat[0];
    mouse_stat=stat[1];
    keyboard_stat=stat[2];
    monitor_stat=stat[3];
    cpu_stat=stat[4];

    }

    void transfer_2(string sym, vector<list<string> > v)
    {
        
        sys_no=sym;

        for(vtr=v.begin();vtr!=v.end();vtr++)
        {
            stat[distance(v.begin(),vtr)]=(*vtr).back();
        }
        compare_stat();
    }



    void transfer()
    {
        int i;
           vector <list<string> > v;
           list<string> l;
           for( i=0;i<5;i++)
           {
           l.push_back(comp[i]);
            l.push_back(stat[i]);
            v.push_back(l);
            l.clear();

        }
            sys.insert(pair<string,vector<list<string> > >(sys_no,v));
        }

void input()
{
    int i;
    string s;

    cout<<"Enter system no.";
    getline(cin,sys_no);

        for(i=0;i<4;i++)
        {
            cout<<"Enter the stat of"<< comp[i+1]<<endl;
            cout<<"w for working"<<'\n'<<"nw for not working"<<endl;
            getline(cin,s);
            if(s=="w")
            {
                stat[i+1]="Working";
            }
            else
            if(s=="nw")
            {
                stat[i+1]="Not Working";
            }
            else
            {
                cout<<"Wrong input";
                break;
            }
        }
            compare_stat();
            
}
    

      void compare_stat()
    {
        int k=1,i;
        for(i=0;i<4;i++)
        {
            if(stat[i+1]!="Working")
                k=0;
        }
        if(k==1)
        {
            stat[0]="Working";
        }
        else
        {
            stat[0]="Not Working";
        }
        }
    };
class cal: public system
{
public:
    void write(string fn)
    {
    fstream file;
    file.open(fn,ios::app|ios::out|ios::binary);
    system a;
    a.input();
    a.address_back();
    file.write((char*)&a,sizeof(a));
    file.close();
     }

    int read(string fn)
    {
    int i,itr;
    fstream file;
    file.open(fn,ios::in|ios::binary);
    file.seekg(0,ios::end);
    if(file.tellg()<1)
    {
        cout<<"There are no systems in the lab"<<endl;
        return 0;
    }
    
   else
   {
    file.seekg(0,ios::beg);
    system a;
   file.seekg(0);
    while(file.read((char*)&a,sizeof(a)))
    {
        a.address();
        a.transfer();
    }
   
   file.close();
   return 1;
    }
    }

    void write_upd(string fn)
    {
    fstream file;
    file.open(fn,ios::out|ios::trunc|ios::binary);
    file.close();
    file.open(fn,ios::out|ios::app|ios::binary);

    for(itr=sys.begin();itr!=sys.end();itr++)
    {
        system a;
        a.transfer_2(itr->first,itr->second);
        a.address_back();
        file.write((char*)&a,sizeof(a));
    }
    file.close();
    }

    void display()
    {
    int i;
     for(itr=sys.begin();itr!=sys.end();itr++)
      {
        cout<<"System No.="<<itr->first<<'\n';
        for(vtr=itr->second.begin();vtr!=itr->second.end();vtr++)
           {
            cout<<(*vtr).front()<<'-'<<(*vtr).back()<<endl;
            }
            cout<<'\n';
        }
    }

void update(string lb)
{
    string s,s1,s2,s3;
    int i,k=1;
    cout<<"Enter the system no. to be updated"<<'\n';
    getline(cin,s);
    cout<<"Enter the component whose status is  to be updated"<<'\n';
    getline(cin,s1);
    cout<<"Enter the new status"<<'\n';
    cout<<"w for working"<<'\n'<<"nw for not working"<<endl;
    getline(cin,s2);
                if(s2=="w")
            {
                s3="Working";
            }
            else
            if(s2=="nw")
            {
                s3="Not Working";
            }
            else
            {
                cout<<"Wrong input";
                k=0;
            }

   if(k==1)
   {
    itr=sys.find(s);
    for(vtr=itr->second.begin();vtr!=itr->second.end();vtr++)
    {
        if((*vtr).front()==s1)
        {
            (*vtr).back()=s3;
        }
    }
    write_upd(lb);
}
}

void search()
{
    string s;
    int i;
    cout<<"enter the system no. to be searched"<<'\n';
    getline(cin,s);
    itr=sys.find(s);
    for(vtr=itr->second.begin();vtr!=itr->second.end();vtr++)
    {
           cout<<(*vtr).front()<<'-'<<(*vtr).back()<<endl;
        }
            cout<<'\n';
        
    }

void del(string lb)
{
    string s;
    cout<<"Enter the system no. to be deleted"<<'\n';
    getline(cin,s);
    itr=sys.find(s);
    sys.erase(itr);
    cout<<"deleted"<<'\n';
    write_upd(lb);
    }

    void choice(int n)
    {
       string lbs[6]={"lab_1.dat","lab_2.dat","lab_3.dat","lab_4.dat","lab_5.dat","lab_6.dat"};
       string lb;
       int a,k;
        cout<<setw(30)<<" No. of labs"<<endl<<endl;
        cout<<" 1: lab1 "<<endl<<endl
         <<"2 : lab2"<<endl<<endl
         <<"3 : lab3"<<endl<<endl
         <<"4 : lab4"<<endl<<endl
         <<"5 : lab5"<<endl<<endl
         <<"6 : lab6"<<endl<<endl;
        cout<<"Enter the no. corresponding the lab :";
        cin>>a;
        char ch=getchar();
        lb=lbs[a-1];

        switch (n)
    {
    case 1 :
        sys.clear();
        k=read(lb);
        if(k==1)
        display();
        break;
       
     case 2 :
      write(lb);
        break;
         
     case 3 :
         sys.clear();
            k=read(lb);
        if(k==1)
          update(lb);
        break;

     case 4 :
         sys.clear();
            k=read(lb);
        if(k==1)
          search();
        break;

     case 5 :
        sys.clear();
           k=read(lb);
        if(k==1)
          del(lb);
        break;

        }
    }

    };
void user_resolved_complaints()
{
    string line;
    cout << setw(40) << "THE RESOLVED COMPLAINTS " << endl;
    cout << "======================================================" << endl
         << endl;
    fstream file;
    file.open("resolved.txt", ios::in);
    while (getline(file, line))
    {
        cout << line << endl
             << endl;
    }
}
void finally_counted_complaints()
{
    int count = 001;
    string line, app_line, yellow;
    fstream file1, file2;
    file1.open("complaint.txt", ios::in);
    file2.open("complaints.txt", ios::app | ios::out);
    while (getline(file1, line))
    {
        yellow = to_string(count);
        app_line = yellow + "     " + line;
        file2 << app_line << endl;
        count++;
        yellow.clear();
    }
}
void resolve_complaints()
{
    void finally_counted_complaints();
    fstream file1, file2, file3;
    string line;
    file1.open("complaints.txt", ios::in);
    file2.open("unresolved_complaint.txt", ios::out);
    file3.open("resolved.txt", ios::app);
    cout << endl
         << setw(30) << "COMPLAINTS" << endl
         << endl;
    /* while (file1.eof() == 0)
     {
         getline(file1, line);
         cout << line << endl;
     }
     cout << endl
          << "===========================================================" << endl;
     line.clear(); */
    string numstr, yellow;
    int num;
    cout << "Enter Complaint Number : ";
    cin >> num;
    numstr = to_string(num);
    int a = numstr.size();
    while (file1.eof() == 0)
    {
        getline(file1, line);
        yellow = line.substr(0, a);
        if (yellow != numstr)
        {
            file2 << line << endl;
        }
        else
        {
            file3 << line << endl;
        }
    }
    file1.close();
    file2.close();
    file3.close();
    remove("complaints.txt");
    rename("unresolved_complaint.txt", "complaints.txt");

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
void particular_string_to_file_copy(void)
{
    string LabNo, line;
    cout << endl
         << "Enter the Lab Number : ";
    cin >> LabNo;
    // check lab no
    fstream myfile;
    myfile.open("complaint.txt", ios::app | ios::in);
    cout << endl
         << setw(40) << " COMPLAINTS OF LAB " << LabNo << endl;
    cout << "==================================================================" << endl
         << endl;
    while (myfile.eof() == 0)
    {
        getline(myfile, line);
        int a = line.find(LabNo);
        if (a == 0)
        {
            cout << line << endl
                 << endl;
        }
    }
    cout << "====================================================================" << endl;
}
void view_complaints()
{
    string line;
    ifstream file1;
    file1.open("complaint.txt", ios::in);
    while (file1.eof() == 0)
    {
        getline(file1, line);
        cout << line << endl
             << endl;
    }
}
void general_file_store(string LabNo, string complaint)
{
    string final;
    final = LabNo + " - " + complaint;
    fstream myfile;
    myfile.open("complaint.txt", ios::app);
    myfile << final << endl;
}
void file_store(string LabNo, string system, string device, string complaint)
{
    string final;
    final = LabNo + " " + system + " - " + device + " - " + complaint;
    fstream myfile;
    myfile.open("complaint.txt", ios::app);
    myfile << final << endl;
}
void generic_complaints(void)
{
    cout << setw(30) << "GENERAL COMPLAINTS" << endl
         << endl;
    string LabNo, system, device, complaint;
    cout << "Enter Lab No : " << endl;
    cin >> LabNo;
    // check if a Lab No is valid or not
    int n;
    cout << setw(20) << " MENU " << endl
         << endl
         << endl;
    cout << "1 : Complaints related to Mouse " << endl
         << endl
         << "2 : Complaints related to CPU " << endl
         << endl
         << "3 : Complaints related to Mointer " << endl
         << endl
         << "4 : Complaints related to Keyboard " << endl
         << endl
         << "5 : Some Other general complaints " << endl
         << endl
         << "6 : Quit " << endl
         << endl;
    ;
    cout << setw(15) << "Enter appropriate number : ";

    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    switch (n)
    {
    case 1:
    {
        cout << endl
             << "=====================================================================" << endl
             << endl;
        cout << setw(30) << "MOUSE" << endl;
        cout << "Enter System No : ";
        cin >> system;
        // check system id is valid or not
        device = "Mouse";
        int m;
        cout << endl
             << setw(20) << "MENU" << endl
             << endl;
        ;
        cout << "1 : Slow Working " << endl
             << endl
             << "2 : Some Wire is Broken " << endl
             << endl
             << "3 : Socket in Which the mouse is pluged in is not working " << endl
             << endl;
        cout << "Enter an appropriate number : " << endl;
        cin >> m;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:
        {
            complaint = "Slow Working";
        }
        break;
        case 2:
        {
            complaint = "Some Wire is Broken ";
        }
        break;
        case 3:
        {
            complaint = "Socket in Which the mouse is pluged in is not working";
        }
        break;
        default:
        {
            cout << "Inavlid Input " << endl;
            exit(1);
        }
        }
        file_store(LabNo, system, device, complaint);
        cout << "YOUR COMPLAINT HAS BEEN SUCCESSFULLY DONE " << endl;
    }
    break;
    case 2:
    {
        cout << endl
             << "=====================================================================" << endl
             << endl;
        cout << setw(30) << "CPU" << endl;
        cout << "Enter System No : ";
        cin >> system;
        // check if the system number is valid or not
        device = "CPU";
        int m;
        cout << endl
             << setw(20) << "MENU" << endl;
        cout << "1 : Slow Working " << endl
             << endl
             << "2 : Some Wire is Broken " << endl
             << endl
             << "3 : Sockets in CPU are not working " << endl
             << endl;
        cout << "Enter an appropriate number : " << endl;
        cin >> m;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:
        {
            complaint = "Slow Working";
        }

        break;
        case 2:
        {
            complaint = "Some Wire is Broken ";
        }
        break;
        case 3:
        {
            complaint = "Sockets in CPU are not working";
        }
        break;
        default:
        {
            cout << "Inavlid Input " << endl;
            exit(1);
        }
        }
        file_store(LabNo, system, device, complaint);
        cout << "YOUR COMPLAINT HAS BEEN SUCCESSFULLY DONE " << endl;
    }
    break;
    case 3:
    {
        cout << endl
             << "=====================================================================" << endl
             << endl;
        cout << setw(30) << "MOINTER" << endl
             << endl;
        cout << "Enter System No : ";
        cin >> system;
        // check if the system number is valid or not
        device = "Mointer";
        int m;
        cout << endl
             << setw(20) << "MENU" << endl;
        cout << "1 : Slow Working " << endl
             << endl
             << "2 : Some Wire is Broken " << endl
             << endl
             << "3 : Sockets not working " << endl
             << endl
             << "4 : Blurred Screen " << endl
             << endl;
        cout << "Enter an appropriate number : " << endl;
        cin >> m;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:
        {
            complaint = "Slow Working";
        }
        break;
        case 2:
        {
            complaint = "Some Wire is Broken ";
        }
        break;
        case 3:
        {
            complaint = "Sockets not working";
        }
        break;
        case 4:
        {
            complaint = "Blurred Screen ";
        }
        break;
        default:
        {
            cout << "Inavlid Input " << endl;
            exit(1);
        }
        }
        file_store(LabNo, system, device, complaint);
        cout << "YOUR COMPLAINT HAS BEEN SUCCESSFULLY DONE " << endl;
    }
    break;
    case 4:

    {
        cout << endl
             << "=====================================================================" << endl
             << endl;
        cout << setw(30) << "KEYBOARD" << endl
             << endl;
        cout << "Enter System No : ";
        cin >> system;
        // check if the system number is valid or not
        device = "Keyboard";
        int m;
        cout << endl
             << setw(20) << "MENU" << endl;
        cout << "1 : Slow Working " << endl
             << endl
             << "2 : Some Wire is Broken " << endl
             << endl
             << "3 : Keys are Coming off " << endl
             << endl;
        cout << "Enter an appropriate number : " << endl;
        cin >> m;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:
        {
            complaint = "Slow Working";
        }
        break;
        case 2:
        {
            complaint = "Some Wire is Broken ";
        }
        break;
        case 3:
        {
            complaint = "Keys are Coming off ";
        }
        break;
        default:
        {
            cout << "Inavlid Input " << endl;
            exit(1);
        }
        }
        file_store(LabNo, system, device, complaint);
        cout << "YOUR COMPLAINT HAS BEEN SUCCESSFULLY DONE " << endl;
    }
    break;
    case 5:
    {
        cout << endl
             << "=====================================================================" << endl
             << endl;
        cout << setw(30) << "SOME OTHER COMPLAINTS" << endl
             << endl;
        int m;
        cout << endl
             << setw(20) << "MENU" << endl;
        cout << "1 : Short Circuit " << endl
             << endl
             << "2 : Switches in Lab Not working " << endl
             << endl
             << "3 : Not enough Chairs  " << endl
             << endl;
        cout << "Enter an appropriate number : " << endl;
        cin >> m;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:

        {
            complaint = "Short Circuit ";
        }

        break;
        case 2:
        {
            complaint = "Switches in Lab Not working ";
        }

        break;
        case 3:
        {
            complaint = "Not enough Chairs ";
        }

        break;
        default:
        {
            cout << "Inavlid Input " << endl;
            exit(1);
        }
        }
        general_file_store(LabNo, complaint);
        cout << "YOUR COMPLAINT HAS BEEN SUCCESSFULLY DONE " << endl;
    }
    break;
    case 6:
        break;
    default:
        cout << "Invalid Input " << endl;
    }
}
class Admin;
class Login
{
public:
    virtual void setID(void){};
    virtual void perform(void){};
};

class Student : public Login,cal
{
protected:
    int input;
    string ID;

public:
    int complaint;
    // Student(string id, int option): Login(id){
    // input = option;
    // }
    void setID()
    {
        cout << "Enter your ID :" << endl;
        cin >> ID;
    }
    void perform()
    {
        cout << "What operation would you like to perform :" << endl
             << "1.See system status" << endl
             << "2.Enter a complaint" << endl
             << "3.View your complaint Status" << endl;
        cin >> input;
        switch (input)
        {
        case 1:
        int k;
        cout<<"1.View status of whole lab"<<endl
            <<"2.View status of a particular system"<<endl;
        cin>>k;
        if(k==1)
            cal :: choice(1);
        if(k==2)
            cal :: choice(4);
            break;
        case 2:
            cout << "Which type of complaint you want to register :" << endl
                 << "1.System related" << endl
                 << "2.General complaint" << endl;
            cin >> complaint;
            switch (complaint)
            {
            case 1:
                int ab;
                cout << "Which part of the system is not working :" << endl
                     << "1.Mouse" << endl
                     << "2.Keyboard" << endl
                     << "3.Monitor" << endl
                     << "4.CPU" << endl;
                break;
            case 2:
                generic_complaints();
            }
            break;
        case 3:
           // cout << "Your complaint status is : " << endl;
            user_resolved_complaints();
            break;

        default:
            cout << "INVALID REQUEST!!!!" << endl;

            break;
        }
    }
};

class Admin : public Login,cal
{
protected:
    string identity, id;
    int input;
    string replace;

public:
    // Admin(string id, int option): Login(id){
    //     input = option;
    // }
    void setID()
    {
        cout << "ENter your ID :" << endl;
        cin >> id;
    }
    void perform()
    {
        cout << "What operation would you like to perform :" << endl
             << "1. View system" << endl
             << "2.View complaints" << endl
             << "3.Add a system" << endl
             << "4.Update a system" << endl;
        cin >> input;
        switch (input)
        {
        case 1:
        cal ::choice(1);
            break;
        case 2:
            int ip;
            cout << "which complaint you want to see " << endl
                 << "1.Students complaints" << endl
                 << "2.Resolved complaints";
            cin >> ip;
            if (ip == 1)
            {
                // cout << "Students complaints are " << endl;
                cout << setw(30) << "WELCOME TO COMPLAINT SECTION " << endl
                     << endl;
                cout << setw(20) << "MENU" << endl
                     << endl;
                cout << "1 : To check the complaints of One Particular Lab" << endl
                     << endl
                     << "2 : To check all the complaints " << endl
                     << endl;
                int n;
                cout << "Enter the appropiate number : ";
                cin >> n;
                switch (n)
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
                    cout << "Inavlid Input " << endl;
                }
            }
            else if (ip == 2)
            {
                // cout << "Resolved complaints are " << endl;
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
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
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
            }
            else
            {
                cout << "Invalid request" << endl;
            }
            break;
        case 3:
            //cout << "How many systems would you like to add? :" << endl;
            cal ::choice(2);
        
            break;
        case 4:
            //cout << "Enter system ID to be replaced :" << endl;
            cal ::choice(3);
            break;
        case 5:
            cal :: choice(5);
            break;
        default:
            cout << "Invalid Request!!!!" << endl;
            break;
        }
    }
};



int main()
{
    Student user;
    Admin edit;
    int z;
    cout << "Select login option :" << endl
         << "1.Admin " << endl
         << "2.Student" << endl;
    cin >> z;
    if (z == 1)
    {
        edit.setID();
        edit.perform();
    }
    else if (z == 2)
    {
        user.setID();
        user.perform();
    }
    else
    {
        cout << "invalid choice selected please select again";
    }
    return 0;
}
