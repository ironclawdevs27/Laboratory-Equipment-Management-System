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
string **stat=new string*[5];
vector<string> comp;
vector<string> lbs;
vector<string>::iterator vtr2;

void box();
void space(int i);
void format(int f,string s);

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

    stat[0]=&comp_stat;
    stat[1]=&mouse_stat;
    stat[2]=&keyboard_stat;
    stat[3]=&monitor_stat;
    stat[4]=&cpu_stat;
    }
    void components_labs()
    {
        comp.push_back("Complete Status");
        comp.push_back("Mouse");
        comp.push_back("Keyboard");
        comp.push_back("Monitor");
        comp.push_back("CPU");
        lbs.push_back("cs1.dat");
        lbs.push_back("cs2.dat");
        lbs.push_back("cs3.dat");
        lbs.push_back("cs4.dat");
        lbs.push_back("cs5.dat");
        lbs.push_back("cs6.dat");


    }

    void transfer_2(string sym, vector<list<string> > v)
    { 
        sys_no=sym;
        for(vtr=v.begin();vtr!=v.end();vtr++)
        {
            *stat[distance(v.begin(),vtr)]=(*vtr).back();
        }
        compare_stat();
    }
    void transfer()
    {
        int i;
           vector <list<string> > v;
           list<string> l;
           vtr2=comp.begin();
           for( i=0;i<5;i++)
           {
           l.push_back((*vtr2));
            l.push_back(*stat[i]);
            v.push_back(l);
            l.clear();
            vtr2++;

        }
            sys.insert(pair<string,vector<list<string> > >(sys_no,v));
        }

void input()
{
    int i;
    string s;
     cout<<endl;space(44);
    cout<<"Enter system no."<<'\t';
    getline(cin,sys_no);
            cout<<endl<<endl;
            space(44);
            cout<<"* * PRESS * *  : "<<'\t'<< "'w' for working" <<'\t'<<"    : 'nw' for not working"<<endl<<endl<<endl;
            vtr2=comp.begin()+1;
        for(i=1;i<5;i++) 
        {
            space(44);
            cout<<"Enter the status of "<< (*vtr2)<<" :" <<'\t'<<'\t';
            // cout<<" w for working "<<'\n'<<" nw for not working"<<endl;
            getline(cin,s);
            cout<<endl;
            if(s=="w")
            {
                *(stat[i])="Working";
            }
            else
            if(s=="nw")
            {
                *(stat[i])="Not Working";
            }
            else
            {
                try{
                cout<<setw(64)<<"Wrong input";
                throw 1;
            }
            catch(int x)
            {
                throw;
            }
            }
            vtr2++;
        }

            compare_stat();
            
}
    

      void compare_stat()
    {
        int k=1,i;
        for(i=1;i<5;i++)
        {
            if(*(stat[i])!="Working")
                k=0;
        }
        if(k==1)
        {
            *(stat[0])="Working";
        }
        else
        {
            *(stat[0])="Not Working";
        }
        }
    };
class cal: public system
{
public:
    void write(string fn)
    {
        int k=1;
    fstream file;
    file.open(fn,ios::app|ios::out|ios::binary);
    system a;
    a.address();
    try
    {
    a.input();
}
catch(int x)
{
    k=0;
     }
     if(k!=0)
 file.write((char*)&a,sizeof(a));
 }

    int read(string fn)
    {
    int i,itr;
    fstream file;
    file.open(fn,ios::in|ios::binary);
    file.seekg(0,ios::end);
    if(file.tellg()<1)
    {
        cout<<endl;
        format(60,"*");
        cout<<"There are no systems in this lab !";format(65,"*");
        cout<<endl<<endl;
        return 0;
    }
    
   else
   {
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
        a.address();
        a.transfer_2(itr->first,itr->second);
        file.write((char*)&a,sizeof(a));
    }
    file.close();
    }


    void display_all()
    {
        int total=0,count_w=0;
        total=sys.size();
        cout<<"Total no. of systems = "<<total<<endl;
        for(itr=sys.begin();itr!=sys.end();itr++)
        {
            vtr=itr->second.begin();
            if((*vtr).back()=="Working")
                count_w++;
    }
    cout<<"No. of working systems= "<<count_w<<endl;
    cout<<"No. of non working systems="<<(total-count_w)<<endl;
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

    void display_working()
    {
        int total=0,count_w=0;
        total=sys.size();
        cout<<"Total no. of systems = "<<total<<endl;
        for(itr=sys.begin();itr!=sys.end();itr++)
        {
            vtr=itr->second.begin();
            if((*vtr).back()=="Working")
                count_w++;
    }
    cout<<"No. of working system= "<<count_w<<endl;
        for(itr=sys.begin();itr!=sys.end();itr++)
        {
            vtr=itr->second.begin();
            if((*vtr).back()=="Working")
            {
            for(vtr=itr->second.begin();vtr!=itr->second.end();vtr++)
            {
                cout<<(*vtr).front()<<'-'<<(*vtr).back()<<endl;
            } 
            cout<<'\n';   
        }
    }
}
void display_non_working()
    {
        int total=0,count_nw=0;
        total=sys.size();
        cout<<"Total no. of systems = "<<total<<endl;
        for(itr=sys.begin();itr!=sys.end();itr++)
        {
            vtr=itr->second.begin();
            if((*vtr).back()=="Not Working")
                count_nw++;
    }
    cout<<"No. of non  working system= "<<count_nw<<endl;
        for(itr=sys.begin();itr!=sys.end();itr++)
        {
            vtr=itr->second.begin();
            if((*vtr).back()=="Not Working")
            {
            for(vtr=itr->second.begin();vtr!=itr->second.end();vtr++)
            {
                cout<<(*vtr).front()<<'-'<<(*vtr).back()<<endl;
            } 
            cout<<'\n';   
        }
    }
}



void update(string lb)
{
    string s,s1,s2,s3;
    int i,k=1,cp;
    cout<<"Enter the system no. to be updated"<<'\n';
    getline(cin,s);
    if(sys.find(s)!=sys.end())
    {
    cout<<"Enter the component "<<endl<<"1.Mouse"<<endl<<"2.Keyboard"<<endl<<"3.Monitor"<<endl<<"4.CPU"<<'\n';
    cin>>cp;
    getchar();
    vtr2=comp.begin()+cp;
    s1=*vtr2;
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
else
{
    cout<<"No system found"<<endl;
}
}

void search()
{
    string s;
    int i;
    cout<<setw(60)<<"Enter the system no. to be searched"<<'\n';
    getline(cin,s);
    if(sys.count(s))
    {
    itr=sys.find(s);
    for(vtr=itr->second.begin();vtr!=itr->second.end();vtr++)
    {
           cout<<(*vtr).front()<<'-'<<(*vtr).back()<<endl;
        }
            cout<<'\n';
        
    }
else
{
    cout<<setw(60)<<"The system  doesn't exist"<<endl;
}
}

void del(string lb)
{
    string s;
    cout<<"Enter the system no. to be deleted"<<'\n';
    getline(cin,s);
    if(sys.count(s))
    {
    itr=sys.find(s);
    sys.erase(itr);
    cout<<"deleted"<<'\n';
    write_upd(lb);
}
else
{
    cout<<"The system doesn't exist"<<endl;
}
    }

    void choice(int n)
    {
        try
        {
        components_labs();
       vtr2=lbs.begin();
       string lb;
       int a,k;
       cout<<endl;
       space(70);
        cout<<" | SELECT LAB | "<<endl<<endl<<endl;
        cout<<setw(65)<<" 1: Operating System  "<<'\t'<<'\t'
         <<"2 : OOPS Lab 1"<<'\t'<<'\t'
         <<"3 : OOPS Lab 2"<<endl<<endl
         <<setw(57)<<"4 : Database "<<'\t'<<'\t'<<'\t'
         <<"5 : Software "<<'\t'<<'\t'
         <<"6 : lab6"<<endl<<endl<<endl;
        cout<<setw(84)<<"Enter the no. corresponding to the lab :"<<'\t';
        try
        {
        cin>>a;
        char ch=getchar();
        if (!(a>=1 &&a<=6))
            throw 1;   
    }
    catch(int x)
    {
    throw;
}
    
        lb=*(vtr2+(a-1));

        switch (n)
    {
    case 1 :
        sys.clear();
        k=read(lb);
        if(k==1)
        {
            cout<<k<<endl;
        display_all();
    }
        break;
       
     case 2 :
     int n;
     char ch;
     cout<<endl<<endl;
        space(44);
         cout << "How many systems would you like to add? :" << '\t';
         try
         {
        cin>>n;
        ch=getchar();
        if(n<0)
            throw 1;
          }
          catch(int x)
          {
          throw;
      }
        for(int i=0;i<n;i++)
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
    case 6 :
         sys.clear();
         k=read(lb);
         if(k==1)
            display_working();
         break;
    case 7:
    sys.clear();
    k=read(lb);
    if(k==1)
        display_non_working();
    break;
        }
    }
    
    catch(int x)
    {
        cout<<"Invalid input"<<endl;
    }
}

    };




void user_resolved_complaints()
{
    string line;
    cout<<endl;format(65,"-");
    cout<< "THE RESOLVED COMPLAINTS ";format(70,"-");cout << endl<<endl;
    // cout << "======================================================" << endl
        //  << endl;
    fstream file;
    file.open("resolved.txt", ios::in);
    while (getline(file, line))
    {
        cout <<setw(70)<< line << endl
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

    cout <<setw(60)<< "COMPLAINT SUCCESSFULLY RESOLVED AND UPDATED !!!" << endl;
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
         <<setw(67) <<"Enter the Lab Number : "<<'\t';
    cin >> LabNo;
    // check lab no
    fstream myfile;
    myfile.open("complaint.txt", ios::app | ios::in);
    cout << endl<<endl; format(63,"-");
        cout << " COMPLAINTS OF LAB : : " << LabNo ;format(70,"-");
        cout<<endl<<endl;
    while (myfile.eof() == 0)
    {
        getline(myfile, line);
        int a = line.find(LabNo);
        if (a == 0)
        {
            cout <<setw(70)<< line << endl
                 << endl;
        }
    }
}
void view_complaints()
{
    string line;
    ifstream file1;
    file1.open("complaint.txt", ios::in);
    while (file1.eof() == 0)
    {
        getline(file1, line);
        cout << setw(70)<<line << endl
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

class Login
{
public:
    virtual void setID(void){};
    virtual void perform(void){};
};

class Student : public Login,public cal
{
protected:
    int input;
    string ID;

public:
    int complaint, system;
    // Student(string id, int option): Login(id){
    // input = option;
    // }
    void setID()
    {
        cout  <<setw(59)<<endl<<endl<< "Enter your ID :" << '\t';
        cin >> ID;
    }
    void perform()
    {
         int j=1;
        while(j!=0)
        {
                  if(j==0)
                   break;
         cout<<endl<<endl;space(44);
        cout <<"What operation would you like to perform :" << endl<<endl<<endl
             << setw(64)<<"1. See system status" << '\t'<<"\t"
             << "2. Enter a complaint" << '\t'<<'\t'
             <<"3. View your complaint Status" << endl<<endl;
             space(44);
        cin >> input;
        switch (input)
        {
        case 1:
        int k;
        cout<<endl;format(24," - ");
        cout<<" SYSTEM STATUS ";format(23," - ");cout<<endl<<endl;
        cout<<setw(70)<<"1. View status of whole lab"<<'\t'<<'\t'
            <<"2. View status of a particular system"<<endl
            <<"3.View status of Working Systems"<<endl
            <<"4.View status of Non-Working Systems"<<endl;
        cin>>k;
        if(k==1)
            cal :: choice(1);
        if(k==2)
            cal :: choice(4);
        if(k==3)
            cal :: choice(6);
        if(k==4)
            cal :: choice(7);
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
        case 4:
             cout<<"Goodbye!"<<endl;
             j=0;
             break;
        default:
            cout << "INVALID REQUEST!!!!" << endl;
            break;
        }
         if(input!=4)
            {
     cout<<"  1. Go back to Student section"<<endl<<"2.Exit";
      try
    {
    cin>>j;
    if(j==1)
        j=1;
    else if(j==2)
            j=0;
    else 
        throw 1;

}
catch(int x)
{
    cout<<"invalid input....Exiting"<<endl;
    j=0;
}

    }
    }
    }
};

class Admin : public Login,public cal
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
        cout <<setw(59)<<endl<<endl<< "Enter your ID :" << '\t';
        cin >> id;
    }
    void perform()
    {
              int j=1;
        while(j!=0)
        {
            if (j==0)
                break;
        cout<<endl<<endl;space(44);
           cout <<"What operation would you like to perform :" << endl<<endl<<endl
             << setw(58)<<"1. View system" << '\t'<<'\t'<<'\t'
             << "2. View complaints" << endl<<endl
             << setw(59) <<"3. Add a system" << '\t'<<'\t'<<'\t'
             << "4. Modify" << endl<<endl;//add delete and back option

             space(44);
        cin >> input;
        switch (input)
        {
        case 1:
            cal ::choice(1);
            break;
        case 2:
            int ip;
            cout<<endl;
            cout <<setw(76)<< "Which complaint you want to see " << endl<<endl
                 <<setw(66)<< "1. Students complaints" << '\t'<<'\t'<<'\t'
                 << "2. Resolved complaints"<<endl<<endl;
                 space(44);
            cin >> ip;
            if (ip == 1)
            {
                cout<<endl;
                format(62,"-");
                cout << "WELCOME TO COMPLAINT SECTION "; format(65,"-");
                cout<<endl<<endl;space(44);format(10," ~ ");
                cout  << "MENU";format(10," ~ ");
                 cout<<endl<< endl;
                cout <<setw(93)<< "1 : To check the complaints of One Particular Lab" << endl
                     << endl
                     << setw(76)<<"2 : To check all the complaints " << endl
                     << endl;
                int n;
                cout << setw(74)<<"Enter the appropiate number : "<<endl<<endl;
                space(44);

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
                    cout <<setw(70)<< " !! Inavlid Input !!" << endl;
                }
            }
            else if (ip == 2)
            {
                // cout << "Resolved complaints are " << endl;
                int n;cout<<endl;format(59,"-");
                cout << "WELCOME TO RESOLVE COMPLAINT SECTION ";format(63,"-");cout << endl;
               
                    cout<<endl<<endl;space(44);format(10," ~ ");
                cout << "MENU";format(10," ~ ");
                 cout<<endl << endl;
                cout <<setw(70)<< "1 : To resolve a complaint " <<'\t'<<'\t'
                     << "2 : To view already resolved complaints " << endl
                     << endl;
                cout <<setw(72)<< "Enter an appropriate Number : "<<endl<<endl;space(44);
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
                    cout<<endl;
                    space(50);
                    cout << "Invalid Input" << endl;
                }
            }
            else
            {
                cout << "Invalid request" << endl;
            }
            break;
        case 3:
            cal ::choice(2);
            break;
        case 4:
            cal ::choice(3);
            break;
        case 5:
            cal :: choice(5);
            break;
        case 6:
            cout<<"Good Bye!!"<<endl;
            j=0;
            break;
        default:
            cout << "Invalid Request!!!!" << endl;
            break;
        }
            if(input!=6)
            {
        cout<<"  1. Go back to admin section"<<endl<<"2.Exit";
      try
    {
    cin>>j;
    if(j==1)
        j=1;
    else if(j==2)
            j=0;
    else 
        throw 1;

}
catch(int x)
{
    cout<<"invalid input....Exiting"<<endl;
    j=0;
}
    }
    }
    }
};
int main()
{
    Student user;
    Admin edit;
        int j=1;
    while(j!=0)
    {
        if(j==0)
            break;
    int z;
    box();
    cout <<setw(10)<<endl<<setw(251)<<"Select login option :"<< endl<<endl<<endl
         <<'\t'<<setw(45)<<"1. Admin " <<endl<<endl
         <<'\t'<< setw(46)<<"2. Student"<<endl<<endl
         <<"3.Exit"<<endl;
         space(44);
    cin >> z;
    if (z == 1)
    {
        format(60,"-");
        cout<<" YOU HAVE ENTERED THE ADMIN SECTION ";format(60,"-");
        edit.setID();
        edit.perform();
    }
    else if (z == 2)
    {
        format(60,"-");
        cout<<" YOU HAVE ENTERED THE STUDENT SECTION ";format(60,"-");
        cout<<endl<<endl;
        user.setID();
        user.perform();
    }
    else if(z== 3)
    {
        cout<<"Goodbye"<<endl;
        j=0;
    }
    else
    {
        cout<<endl;
        space(50);
        cout<< " ! ! !  Invalid choice selected please select again ! ! !" <<endl<<endl;
    }
    
    if(z!=3)
    {
    format(55,"<");
    cout<<"  1. Go back to login section"<<endl<<"2.Exit";format(60,">");cout<<endl<<endl;
    space(44);
    try
    {
    cin>>j;
    if(j==1)
        j=1;
    else if(j==2)
            j=0;
    else 
        throw 1;

}
catch(int x)
{
    cout<<"invalid input....Exiting"<<endl;
    j=0;
}
}
    
}
cout<<setw(60)<<"Take Care!"<<endl;
    return 0;
}


void box(){
int column=160;
for(int j=0;j<column;j++)
{
    cout<<"=";
}
cout<<endl;
cout<<setw(255)<<" |  LAB MANAGEMENT SYSTEM  | "<<endl<<endl;
for(int j=0;j<column;j++)
{
    cout<<"=";
}
cout<<endl;

}
void space(int sp)
{
for(int i=0;i<sp;i++)
{
    cout<<" ";
}
}
void format(int f,string s)
{
for(int j=0;j<f;j++)
{
    cout<<s;
}
}