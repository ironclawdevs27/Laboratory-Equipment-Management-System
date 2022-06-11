
#include <iostream>
#include<map>
#include<string>
#include<iterator>
#include<algorithm>
#include<set>
#include<vector>
#include<fstream>
#include<list>
#include<iomanip>
using namespace std;
map<string,vector<list<string> > >sys;
map<string,vector<list<string> > >::iterator itr;
vector<list<string> >::iterator vtr;
list<string>::iterator j;
string stat[5];
string comp[5]={"Complete status","Mouse","Keyboard","Monitor","CPU"};
class A
{
	string sys_no;
	string comp_stat;
	string mouse_stat;
	string keyboard_stat;
	string monitor_stat;
	string cpu_stat;


public:
	A()
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
void write(string fn)
{
	fstream file;
	file.open(fn,ios::app|ios::out);
	A a;
	a.input();
	a.address_back();
	file.write((char*)&a,sizeof(a));
	file.close();
}
int read(string fn)
{
	int i,itr;
	fstream file;
	file.open(fn,ios::in);
	file.seekg(0,ios::end);
	if(file.tellg()<1)
	{
		cout<<"There are no systems in the lab"<<endl;
		return 0;
	}

   else
   {
   	file.seekg(0,ios::beg);
	A a;
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

void write_upd(string fn)
{
	fstream file;
	file.open(fn,ios::out|ios::trunc);
	file.close();
	file.open(fn,ios::out|ios::app);

	for(itr=sys.begin();itr!=sys.end();itr++)
    {
    	A a;
    	a.transfer_2(itr->first,itr->second);
    	a.address_back();
    	file.write((char*)&a,sizeof(a));
    }
	file.close();
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

void choice()
{

		string lbs[6]={"l1.txt","l2.txt","l3.txt","l4.txt","l5.txt","l6.txt"};
	   string lb;
	   int a,b=1;
	  

	cout<<setw(30)<<" No. of labs"<<endl<<endl;
        cout<<" 1: lab1 "<<endl<<endl
         <<"2 : lab2"<<endl<<endl
         <<"3 : lab3"<<endl<<endl
         <<"4 : lab4"<<endl<<endl
         <<"5 : lab5"<<endl<<endl
         <<"6 : lab6"<<endl<<endl;
        cout<<"Enter the no. corresponding the lab :";
        cin>>a;
        lb=lbs[a-1];


     while(b!=0)
	   {
	   	if(b==0)
	   		break;
	   	else
	   	{
    int n,k,r;
    char ch;
        cout<<setw(30)<<" MENU "<<endl<<endl;
        cout<<" 1 : Add a System  "<<endl<<endl
         <<"2 : Delete a System  "<<endl<<endl
         <<"3 : Update "<<endl<<endl
         <<"4 : Search "<<endl<<endl
         <<"5 : Display "<<endl<<endl;
        cout<<"Enter an appropriate Number : ";
        cin>>n;
        ch=getchar();

    switch (n)
    {
    case 1 :
    	write(lb);
        break;
     case 2 :
         sys.clear();
    	   k=read(lb);
        if(k==1)
    	  del(lb);
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
     case 5:
         sys.clear();
     	   k=read(lb);
        if(k==1)
        display();
        break;
    default :
        cout<<"Invalid Input"<<endl;
        break;
    }
    cout<<"Enter 0 to end and any other to continue"<<endl;
    cin>>b;
 }
}
}

int main()
{
	choice();
}
