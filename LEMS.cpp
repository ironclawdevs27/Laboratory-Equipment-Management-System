#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <cstring>
#include <ios>
#include <limits>
#include <map>
#include <iterator>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
using namespace std;
map<string, vector<list<string>>> sys;
map<string, vector<list<string>>>::iterator itr;
vector<list<string>>::iterator vtr;
list<string>::iterator j;
string **stat = new string *[5];
vector<string> comp;
vector<string> lbs;
vector<string>::iterator vtr2;
void box();
void space(int i);
void format(int f, string s);
void display_studentlist()
{
    cout << "<<<<<<< Students List >>>>>>>" << endl
         << endl;
    string line;
    ifstream ifile;
    ifile.open("studentsDB.txt");
    int i = 1;
    while (ifile)
    {
        getline(ifile, line);
        cout << i << ". " << line << endl;
        i++;
    }
    cout << endl;
}
void display_adminlist()
{
    cout << "<<<<<<< Admins List >>>>>>>" << endl
         << endl;
    string line;
    ifstream ifile;
    ifile.open("adminsDB.txt");
    int i = 1;
    while (ifile)
    {
        getline(ifile, line);
        cout << i << ". " << line << endl;
        i++;
    }
    cout << endl;
}
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
        sys_no = "";
        comp_stat = "";
        mouse_stat = "";
        keyboard_stat = "";
        monitor_stat = "";
        cpu_stat = "";
    }
    void address()
    {
        stat[0] = &comp_stat;
        stat[1] = &mouse_stat;
        stat[2] = &keyboard_stat;
        stat[3] = &monitor_stat;
        stat[4] = &cpu_stat;
    }
    void components_labs()
    {
        comp.push_back("Complete Status");
        comp.push_back("Mouse          ");
        comp.push_back("Keyboard       ");
        comp.push_back("Monitor        ");
        comp.push_back("CPU            ");
        lbs.push_back("an.dat");
        lbs.push_back("no.dat");
        lbs.push_back("yi.dat");
        lbs.push_back("ng.dat");
        lbs.push_back("ars.dat");
        lbs.push_back("hia.dat");
    }
    void transfer_2(string sym, vector<list<string>> v)
    {
        sys_no = sym;
        for (vtr = v.begin(); vtr != v.end(); vtr++)
            *stat[distance(v.begin(), vtr)] = (*vtr).back();
        compare_stat();
    }
    void transfer()
    {
        int i;
        vector<list<string>> v;
        list<string> l;
        vtr2 = comp.begin();
        for (i = 0; i < 5; i++)
        {
            l.push_back((*vtr2));
            l.push_back(*stat[i]);
            v.push_back(l);
            l.clear();
            vtr2++;
        }
        sys.insert(pair<string, vector<list<string>>>(sys_no, v));
    }
    void input()
    {
        int i;
        string s;
        cout << endl;
        space(44);
        cout << "Enter system no." << '\t' << '\t';
        getline(cin, sys_no);
        cout << endl
             << endl;
        space(44);
        cout << "* * PRESS * *  : " << '\t' << "'w' for working" << '\t' << "    : 'nw' for not working" << endl
             << endl
             << endl;
        vtr2 = comp.begin() + 1;
        for (i = 1; i < 5; i++)
        {
            space(44);
            cout << "Enter the status of " << (*vtr2) << " :" << '\t' << '\t';
            // cout<<" w for working "<<'\n'<<" nw for not working"<<endl;
            getline(cin, s);
            cout << endl;
            if (s == "w")
            {
                *(stat[i]) = "Working";
            }
            else if (s == "nw")
            {
                *(stat[i]) = "Not Working";
            }
            else
            {
                try
                {
                    cout << setw(64) << "! ! ! Wrong input ! ! !" << endl;
                    throw 1;
                }
                catch (int x)
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
        int k = 1, i;
        for (i = 1; i < 5; i++)
        {
            if (*(stat[i]) != "Working")
                k = 0;
        }
        if (k == 1)
        {
            *(stat[0]) = "Working";
        }
        else
        {
            *(stat[0]) = "Not Working";
        }
    }
};
class cal : public system
{
public:
    void write(string fn)
    {
        int k = 1;
        fstream file;
        file.open(fn, ios::app | ios::out | ios::binary);
        system a;
        a.address();
        try
        {
            a.input();
        }
        catch (int x)
        {
            k = 0;
        }
        if (k != 0)
            file.write((char *)&a, sizeof(a));
    }
    int read(string fn)
    {
        int i, itr;
        fstream file;
        file.open(fn, ios::in | ios::binary);
        file.seekg(0, ios::end);
        if (file.tellg() < 1)
        {
            cout << endl;
            format(60, "*");
            cout << "There are no systems in this lab !";
            format(65, "*");
            cout << endl
                 << endl;
            return 0;
        }
        else
        {
            system a;
            file.seekg(0);
            while (file.read((char *)&a, sizeof(a)))
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
        file.open(fn, ios::out | ios::trunc | ios::binary);
        file.close();
        file.open(fn, ios::out | ios::app | ios::binary);
        for (itr = sys.begin(); itr != sys.end(); itr++)
        {
            system a;
            a.address();
            a.transfer_2(itr->first, itr->second);
            file.write((char *)&a, sizeof(a));
        }
        file.close();
    }
    void display_all()
    {
        int total = 0, count_w = 0;
        total = sys.size();
        cout << endl;
        space(44);
        cout << "Total no. of systems =         " << '\t' << total << endl
             << endl;
        space(44);
        for (itr = sys.begin(); itr != sys.end(); itr++)
        {
            vtr = itr->second.begin();
            if ((*vtr).back() == "Working")
                count_w++;
        }
        cout << "No. of working systems =     " << '\t' << count_w << endl
             << endl;
        space(44);
        cout << "No. of non working systems = " << '\t' << (total - count_w) << endl
             << endl;
        space(44);
        for (itr = sys.begin(); itr != sys.end(); itr++)
        {
            cout << endl;
            space(44);
            cout << "System No. :                  " << '\t' << itr->first << endl
                 << endl;
            for (vtr = itr->second.begin(); vtr != itr->second.end(); vtr++)
            {
                space(44);
                cout << (*vtr).front() << '-';
                space(15);
                cout << (*vtr).back() << endl
                     << endl;
            }
            cout << '\n';
        }
    }
    void display_working()
    {
        int total = 0, count_w = 0;
        total = sys.size();
        cout << "Total no. of systems = " << total << endl;
        for (itr = sys.begin(); itr != sys.end(); itr++)
        {
            vtr = itr->second.begin();
            if ((*vtr).back() == "Working")
                count_w++;
        }
        cout << "No. of working system= " << count_w << endl;
        for (itr = sys.begin(); itr != sys.end(); itr++)
        {
            vtr = itr->second.begin();
            if ((*vtr).back() == "Working")
            {
                for (vtr = itr->second.begin(); vtr != itr->second.end(); vtr++)
                {
                    cout << (*vtr).front() << '-' << (*vtr).back() << endl;
                }
                cout << '\n';
            }
        }
    }
    void display_non_working()
    {
        int total = 0, count_nw = 0;
        total = sys.size();
        cout << "Total no. of systems = " << total << endl;
        for (itr = sys.begin(); itr != sys.end(); itr++)
        {
            vtr = itr->second.begin();
            if ((*vtr).back() == "Not Working")
                count_nw++;
        }
        cout << "No. of non  working system= " << count_nw << endl;
        for (itr = sys.begin(); itr != sys.end(); itr++)
        {
            vtr = itr->second.begin();
            if ((*vtr).back() == "Not Working")
            {
                for (vtr = itr->second.begin(); vtr != itr->second.end(); vtr++)
                {
                    cout << (*vtr).front() << '-' << (*vtr).back() << endl;
                }
                cout << '\n';
            }
        }
    }
    void update(string lb)
    {
        string s, s1, s2, s3;
        int i, k = 1, cp;
        char ch;
        cout << endl;
        space(44);
        cout << "Enter the system no. to be modified :" << '\t' << '\t';
        getline(cin, s);
        if (sys.find(s) != sys.end())
        {
            cout << endl;
            space(44);
            cout << "Enter the component " << endl
                 << endl;
            space(44);

            cout << "1. Mouse" << '\t' << '\t'

                 << "2. Keyboard" << '\t'

                 << "3. Monitor" << '\t'

                 << "4. CPU" << endl
                 << endl;
            space(44);
            cin >> cp;
            getchar();
            if (cp >= 1 && cp <= 4)
            {
                vtr2 = comp.begin() + cp;
                s1 = *vtr2;
                cout << endl;
                space(44);
                cout << "Enter the new status" << '\n'
                     << endl;
                space(44);

                cout << " * PRESS * : w for working" << '\t' << '\t' << "nw for not working" << endl
                     << endl;
                space(44);
                getline(cin, s2);
                if (s2 == "w")
                {
                    s3 = "Working";
                }
                else if (s2 == "nw")
                {
                    s3 = "Not Working";
                }
                else
                {
                    cout << setw(60) << "Wrong input" << endl;
                    k = 0;
                }
                if (k == 1)
                {
                    itr = sys.find(s);
                    for (vtr = itr->second.begin(); vtr != itr->second.end(); vtr++)
                        if ((*vtr).front() == s1)
                            (*vtr).back() = s3;
                    write_upd(lb);
                }
            }
            else
            {
                cout << endl;
                space(70);
                cout << "Wrong Input !!" << endl;
            }
        }
        else
        {
            cout << endl
                 << endl;
            space(44);
            cout << "No system found ! ! ! " << endl;
        }
    }
    void search()
    {
        string s;
        int i;
        cout << endl;
        space(44);
        cout << "Enter the system no. to be searched" << '\t' << '\t';
        getline(cin, s);
        if (sys.count(s))
        {
            itr = sys.find(s);
            for (vtr = itr->second.begin(); vtr != itr->second.end(); vtr++)
                cout << (*vtr).front() << '-' << (*vtr).back() << endl;
            cout << '\n';
        }
        else
            cout << endl;
        space(70);
        cout << "The system  doesn't exist ! !" << endl;
    }
    void del(string lb)
    {
        string s;
        cout << "Enter the system no. to be deleted" << '\n';
        getline(cin, s);
        if (sys.count(s))
        {
            itr = sys.find(s);
            sys.erase(itr);
            cout << "deleted" << '\n';
            write_upd(lb);
        }
        else
            space(44);

        cout << "The system doesn't exist ! ! " << endl;
    }
    void choice(int n)
    {
        try
        {
            components_labs();
            vtr2 = lbs.begin();
            string lb;
            int a, k;
            cout << endl;
            space(77);
            cout << " | SELECT LAB | " << endl;
            space(77);
            format(16, "-");
            cout << endl
                 << endl
                 << endl;
            cout << setw(65) << " 1: Operating System  " << '\t' << '\t'
                 << "2 : OOPS Lab 1" << '\t' << '\t'
                 << "3 : OOPS Lab 2" << endl
                 << endl
                 << setw(57) << "4 : Database " << '\t' << '\t' << '\t'
                 << "5 : Software " << '\t' << '\t'
                 << "6 : Microprocessor" << endl
                 << endl
                 << endl;
            cout << setw(84) << "Enter the no. corresponding to the lab :" << '\t';
            try
            {
                cin >> a;
                char ch = getchar();
                if (!(a >= 1 && a <= 6))
                    throw 1;
            }
            catch (int x)
            {
                throw;
            }
            lb = *(vtr2 + (a - 1));
            switch (n)
            {
            case 1:
                sys.clear();
                k = read(lb);
                if (k == 1)
                {
                    cout << k << endl;
                    display_all();
                }
                break;
            case 2:
                int n;
                char ch;
                cout << endl
                     << endl;
                space(44);
                cout << "How many systems would you like to add? :" << '\t';
                try
                {
                    cin >> n;
                    ch = getchar();
                    if (n < 0)
                        throw 1;
                }
                catch (int x)
                {
                    throw;
                }
                for (int i = 0; i < n; i++)
                    write(lb);
                break;

            case 3:
                sys.clear();
                k = read(lb);
                if (k == 1)
                    update(lb);
                break;

            case 4:
                sys.clear();
                k = read(lb);
                if (k == 1)
                    search();
                break;
            case 5:
                sys.clear();
                k = read(lb);
                if (k == 1)
                    del(lb);
                break;
            case 6:
                sys.clear();
                k = read(lb);
                if (k == 1)
                    display_working();
                break;
            case 7:
                sys.clear();
                k = read(lb);
                if (k == 1)
                    display_non_working();
                break;
            }
        }
        catch (int x)
        {
            cout << endl;
            space(60);
            cout << "Invalid input" << endl;
        }
    }
};
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
    file1.close();
    file2.close();
}
void general_file_store(string LabNo, string complaint)
{
    string final;
    final = LabNo + " - " + complaint;
    fstream myfile;
    myfile.open("complaint.txt", ios::app);
    myfile << final << endl;
    myfile.close();
}
void file_store(string LabNo, string system, string device, string complaint)
{
    string final;
    final = LabNo + " " + system + " - " + device + " - " + complaint;
    fstream myfile;
    myfile.open("complaint.txt", ios::app);
    myfile << final << endl;
    myfile.close();
}
class Login
{
public:
    virtual void setID(void){};
    virtual void perform(void){};
};
class Student : public Login, public cal
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
        cout << setw(59) << endl
             << endl
             << "Enter your ID :" << '\t';
        cin >> ID;
        valid_student(ID);
    }
    void valid_student(string stu)
    {
        transform(stu.begin(), stu.end(), stu.begin(), ::toupper);
        string check = stu.substr(0, 2);
        if (check == "UE" && stu.length() == 8)
        {
            read_studentdb(stu);
            return;
        }
        else
        {
            cout << endl;
            space(44);
            cout << "Invalid Input!" << endl;
            setID();
        }
    }
    void read_studentdb(string s)
    {
        int k = 0;
        string line;
        ifstream ifile;
        ifile.open("studentsDB.txt");
        while (ifile)
        {
            getline(ifile, line);
            if (s.compare(line) == 0)
            {
                cout << "Hello! " << line << " Welcome aboard once again!" << endl;
                return;
            }
        }
        space(44);
        cout << "Invalid Student ID!" << endl
             << endl;
        space(44);
        cout << "Ask Admins to get your Student ID registered in the database!" << endl
             << endl;
        space(44);
        cout << "EXITED FROM THE SYSTEM" << endl
             << endl;
        exit(0);
    }
    void perform()
    {
        int j = 1;
        while (j != 0)
        {
            if (j == 0)
                break;
            cout << endl
                 << endl;
            space(44);
            cout << "What operation would you like to perform :" << endl
                 << endl
                 << endl
                 << setw(73) << "1. See system status         " << '\t' << "\t" << '\t'
                 << "2. Enter a complaint" << endl
                 << endl
                 << setw(73) << "3. View your complaint Status" << '\t' << '\t' << '\t'
                 << "4. Exit " << endl
                 << endl;
            space(44);
            cin >> input;
            switch (input)
            {
            case 1:
            {
                int k;
                cout << endl;
                format(26, " - ");
                cout << " SYSTEM STATUS ";
                format(26, " - ");
                cout << endl
                     << endl;
                cout << setw(70) << " 1. View status of whole lab" << '\t' << '\t'
                     << "        2. View status of a particular system   " << endl
                     << endl;
                space(43);
                cout << "3.View status of Working Systems" << '\t' << '\t'
                     << "4.View status of Non-Working Systems    " << endl
                     << endl;
                space(44);
                cin >> k;
                if (k == 1)
                    cal ::choice(1);
                if (k == 2)
                    cal ::choice(4);
                if (k == 3)
                    cal ::choice(6);
                if (k == 4)
                    cal ::choice(7);
            }
            break;
            case 2:
            {
                cout << endl;
                space(44);
                cout << "Which type of complaint you want to register :" << endl
                     << endl;
                space(44);
                cout << "1. System related" << '\t' << '\t' << '\t'
                     << "2. General complaint" << endl
                     << endl;
                space(44);
                cin >> complaint;
                cout << endl;
                switch (complaint)
                {
                case 1:
                {
                    int ab;
                    cout << setw(85) << "Which part of the system is not working :" << endl
                         << endl;
                    space(44);
                    cout << "1. Mouse   " << '\t' << '\t' << '\t' << "2. Keyboard" << endl
                         << endl;
                    space(44);
                    cout << "3. Monitor " << '\t' << '\t' << '\t' << "4. CPU     " << endl
                         << endl;
                }
                break;
                case 2:
                    generic_complaints();
                }
            }
            break;
            case 3: // cout << "Your complaint status is : " << endl;
                user_resolved_complaints();
                break;
            case 4:
            {
                cout << endl;
                space(70);
                cout << "YOU HAVE EXITED SUCCESSFULLY !" << endl;
                j = 0;
                break;
            default:
                cout << endl;
                space(70);
                cout << "INVALID REQUEST!!!!" << endl;
            }
            break;
            }
        }
        if (input != 4)
        {
            cout << endl;
            format(42, "<");
            cout << "  1. Go back to Student section" << '\t' << '\t' << "2. Exit";
            space(5);
            format(76, ">");
            cout << endl
                 << endl;
            space(44);
            try
            {
                cin >> j;
                if (j == 1)
                    j = 1;
                else if (j == 2)
                    j = 0;
                else
                    throw 1;
            }
            catch (int x)
            {
                cout << "invalid input....Exiting" << endl;
                j = 0;
            }
        }
    }
    void generic_complaints();
    void user_resolved_complaints();
};
class Admin : public Login, public cal
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
        cout << setw(59) << endl
             << endl
             << "Enter your ID :" << '\t';
        cin >> id;
        valid_admin(id);
    }
    void valid_admin(string adm)
    {
        transform(adm.begin(), adm.end(), adm.begin(), ::toupper);
        string check = adm.substr(0, 9);
        if (check == "UIET/CSE/" && adm.length() == 16)
        {
            read_admindb(adm);
            return;
        }
        else
        {
            cout << endl;
            space(44);
            cout << "Invalid Input!" << endl;
            setID();
        }
    }
    void read_admindb(string a)
    {
        int k = 0;
        string line;
        ifstream ifile;
        ifile.open("adminsDB.txt");
        while (ifile)
        {
            getline(ifile, line);
            if (a.compare(line) == 0)
            {
                space(44);
                cout << "Hello! " << line << " Welcome aboard once again!" << endl;
                return;
            }
        }
        cout << endl;
        space(44);

        cout << "Invalid Admin ID!" << endl
             << endl;
        space(44);

        cout << "Contact Admins to get your Admin ID registered in the database!" << endl
             << endl;
        space(44);
        cout << "EXITED FROM THE SYSTEM" << endl
             << endl;
        exit(0);
    }
    void perform()
    {
        int j = 1;
        while (j != 0)
        {
            if (j == 0)
                break;
            cout << endl
                 << endl;
            space(44);
            cout << "What operation would you like to perform :" << endl
                 << endl
                 << endl
                 << setw(58) << "1. View system" << '\t' << '\t' << '\t'
                 << "2. View complaints" << endl
                 << endl
                 << setw(59) << "3. Add a system" << '\t' << '\t' << '\t'
                 << "4. Modify" << endl
                 << endl
                 << setw(62) << "5. Delete a system" << '\t' << '\t' << '\t'
                 << "6. Add ID     " << endl
                 << endl
                 << setw(59) << "7. Delete ID   " << '\t' << '\t' << '\t'
                 << "8. Display all ID's " << endl
                 << endl;
            space(44);
            cout << "9. Exit" << endl
                 << endl;
            // add delete and back option
            space(44);
            cin >> input;
            switch (input)
            {
            case 1:
                cal ::choice(1);
                break;
            case 2:
            {
                int ip;
                cout << endl;
                cout << setw(76) << "Which complaint you want to see " << endl
                     << endl
                     << setw(66) << "1. Students complaints" << '\t' << '\t' << '\t'
                     << "2. Resolved complaints" << endl
                     << endl;
                space(44);
                cin >> ip;
                if (ip == 1)
                {
                    cout << endl;
                    format(62, "-");
                    cout << "WELCOME TO COMPLAINT SECTION ";
                    format(65, "-");
                    cout << endl
                         << endl;
                    space(44);
                    format(10, " ~ ");
                    cout << "MENU";
                    format(10, " ~ ");
                    cout << endl
                         << endl;
                    cout << setw(93) << "1 : To check the complaints of One Particular Lab" << endl
                         << endl
                         << setw(76) << "2 : To check all the complaints " << endl
                         << endl;
                    int n;
                    space(44);
                    cout << "Enter the appropiate number : " << '\t' << '\t';
                    cin >> n;
                    switch (n)
                    {
                    case 1:
                        particular_string_to_file_copy();
                        break;
                    case 2:
                        view_complaints();
                        break;
                    default:
                        cout << setw(70) << " !! Inavlid Input !!" << endl;
                    }
                }
                else if (ip == 2)
                {
                    // cout << "Resolved complaints are " << endl;
                    int n;
                    cout << endl;
                    format(59, "-");
                    cout << "WELCOME TO RESOLVE COMPLAINT SECTION ";
                    format(70, "-");
                    cout << endl;
                    cout << endl
                         << endl;
                    space(43);
                    format(10, " ~ ");
                    cout << "MENU";
                    format(10, " ~ ");
                    cout << endl
                         << endl;
                    cout << setw(70) << "1 : To resolve a complaint " << '\t' << '\t'
                         << "2 : To view already resolved complaints " << endl
                         << endl;
                    cout << setw(73) << "Enter an appropriate Number : " << '\t' << '\t';
                    cin >> n;
                    cout << endl
                         << endl;
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    switch (n)
                    {
                    case 1:
                        resolve_complaints();
                        break;
                    case 2:
                        log_of_resolved_complaints();
                        break;
                    default:
                    {
                        cout << endl;
                        space(64);
                        cout << "Invalid Input" << endl;
                    }
                    }
                }
                else
                    cout << endl;
                space(70);
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
                cal ::choice(5);
                break;

            case 6:
            {
                int adid;
                cout << endl;
                space(44);
                cout << "1. Add Admin ID " << '\t' << '\t' << "2. Add Student ID" << endl
                     << endl;
                space(44);
                cin >> adid;
                if (adid == 1)
                {
                    string s;
                    cout << "Enter Student ID to be registered in UE______ format:" << endl;
                    cin >> s;
                    ofstream file_out;
                    file_out.open("studentsDB.txt", ios_base::app);
                    file_out << endl;
                    file_out << s;
                }
                else if (adid == 2)
                {
                    string a;
                    cout << "Enter Admin ID to be registered in UIET/CSE/ADMIN__ format:" << endl;
                    cin >> a;
                    ofstream file_out;
                    file_out.open("adminsDB.txt", ios_base::app);
                    file_out << endl;
                    file_out << a;
                }
            case 7:
                int delid;
                cout << endl;
                space(44);
                cout << "1. Delete Admin ID " << '\t' << '\t' << "2. Delete Student ID" << endl
                     << endl;
                space(44);
                cin >> delid;
                if (delid == 1)
                {
                    string line, a;
                    ifstream fin;
                    fin.open("adminsDB.txt");
                    ofstream temp;
                    temp.open("temp.txt");
                    cout << "Enter the Admin ID to be removed:" << endl;
                    cin >> a;
                    while (getline(fin, line))
                    {
                        line.replace(line.find(a), a.length(), "");
                        temp << line << endl;
                    }
                    temp.close();
                    fin.close();
                    remove("adminsDB.txt");
                    rename("temp.txt", "adminsDB.txt");
                }
                else if (delid == 2)
                {
                    string line, s;
                    ifstream fin;
                    fin.open("studentsDB.txt");
                    ofstream temp;
                    temp.open("temp.txt");
                    cout << "Enter the Student ID to be removed:" << endl;
                    cin >> s;
                    while (getline(fin, line))
                    {
                        line.replace(line.find(s), s.length(), "");
                        temp << line << endl;
                    }
                    temp.close();
                    fin.close();
                    remove("studentsDB.txt");
                    rename("temp.txt", "studentsDB.txt");
                }
                break;
            case 8:
                display_studentlist();
                display_adminlist();
                break;
            case 9:
            {
                cout << endl;
                format(54, "<");
                cout << "      YOU HAVE SUCCESSFULLY EXITED FROM THE ADMIN SECTION       ";
                format(60, ">");
                cout << endl
                     << endl;
                j = 0;
            }
            break;
            default:
                cout << setw(60) << "Invalid Request!!!!" << endl;
                break;
            }
                if (input != 9)
                {
                    cout << endl;
                    cout << setw(63) << " Choose accordingly " << endl
                         << endl;
                    cout << setw(73) << "  1. Go back to admin section ?";
                    space(15);
                    cout << " 2. Exit ?" << endl
                         << endl;
                    space(44);
                    try
                    {
                        cin >> j;
                        if (j == 1)
                            j = 1;
                        else if (j == 2)
                            j = 0;
                        else
                            throw 1;
                    }
                    catch (int x)
                    {
                        cout << setw(60) << "Invalid Input .... Exiting" << endl;
                        j = 0;
                    }
                }
            }
        }
    }
    void particular_string_to_file_copy();
    void view_complaints();
    void resolve_complaints();
    void log_of_resolved_complaints();
};
void Student::user_resolved_complaints()
{
    string line;
    cout << endl;
    format(65, "-");
    cout << "THE RESOLVED COMPLAINTS ";
    format(70, "-");
    cout << endl
         << endl;
    fstream file;
    file.open("resolved.txt", ios::in);
    while (getline(file, line))
        cout << setw(81) << line << endl
             << endl;
    file.close();
}
void Admin::resolve_complaints()
{
    finally_counted_complaints();
    fstream file1, file2, file3;
    string line;
    file1.open("complaints.txt", ios::in);
    file2.open("unresolved_complaint.txt", ios::out);
    file3.open("resolved.txt", ios::app);
    cout << endl;
    space(72);
    cout << "COMPLAINTS" << endl
         << endl;

    string numstr, yellow;
    int num;
    space(44);
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
    cout << endl;
    cout << endl;
    space(50);
    cout << "! ! ! COMPLAINT SUCCESSFULLY RESOLVED AND UPDATED ! ! !" << endl
         << endl;
}
void Admin::log_of_resolved_complaints()
{
    ifstream file;
    string line;
    file.open("resolved.txt", ios::in);
    cout << endl;
    space(66);
    cout << "LOG OF RESOLVED COMPLAINTS " << endl
         << endl;
    format(170, "-");
    cout << endl
         << endl;
    while (file.eof() == 0)
    {
        space(44);
        getline(file, line);
        cout << line << endl
             << endl;
    }
    file.close();
}
void Admin::particular_string_to_file_copy(void)
{
    string LabNo, line;
    cout << endl
         << setw(67) << "Enter the Lab Number : " << '\t';
    cin >> LabNo;
    // check lab no
    fstream myfile;
    myfile.open("complaint.txt", ios::app | ios::in);
    cout << endl
         << endl;
    format(63, "-");
    cout << " COMPLAINTS OF LAB : : " << LabNo;
    format(70, "-");
    cout << endl
         << endl;
    while (myfile.eof() == 0)
    {
        getline(myfile, line);
        int a = line.find(LabNo);
        if (a == 0)
            cout << setw(70) << line << endl
                 << endl;
    }
    myfile.close();
}
void Admin::view_complaints()
{
    string line;
    ifstream file1;
    file1.open("complaint.txt", ios::in);
    while (file1.eof() == 0)
    {
        getline(file1, line);
        cout << setw(70) << line << endl
             << endl;
    }
    file1.close();
}
void Student::generic_complaints(void)
{
    format(40, "- ");
    cout << "GENERAL COMPLAINTS";
    format(40, "- ");
    cout << endl
         << endl;
    space(44);
    string LabNo, system, device, complaint;
    cout << "Enter Lab No : " << '\t' << '\t';
    cin >> LabNo;
    cout << endl;
    // check if a Lab No is valid or not
    int n;
    format(42, "~ ");
    cout << " MENU ";
    format(44, "~ ");
    cout << endl
         << endl
         << endl;
    cout << setw(80) << "1 : Complaints related to Mouse    " << endl
         << endl
         << setw(80) << "2 : Complaints related to CPU      " << endl
         << endl
         << setw(80) << "3 : Complaints related to Mointer  " << endl
         << endl
         << setw(80) << "4 : Complaints related to Keyboard " << endl
         << endl
         << setw(82) << "5 : Some Other general complaints    " << endl
         << endl;
    space(45);
    cout << "6 : Quit   " << endl
         << endl;
    space(44);
    cout << "Enter appropriate number : " << '\t' << '\t';
    cin >> n;
    cout << endl
         << endl;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    switch (n)
    {
    case 1:
    {
        cout << endl;
        format(42, "* ");
        cout << "MOUSE";
        format(44, "* ");
        cout << endl
             << endl;
        space(44);
        cout << "Enter System No : " << '\t' << '\t';
        cin >> system;
        // check system id is valid or not
        device = "Mouse";
        int m;
        cout << endl
             << setw(100) << "SELECT COMPLAINT " << endl
             << endl;
        cout << setw(61) << "1 : Slow Working " << endl
             << endl
             << setw(68) << "2 : Some Wire is Broken " << endl
             << endl
             << setw(102) << "3 : Socket in Which the mouse is pluged in is not working " << endl
             << endl;
        space(44);
        cout << "Enter an appropriate number : " << '\t' << '\t';
        cin >> m;
        cout << endl;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:
            complaint = "Slow Working";
            break;
        case 2:
            complaint = "Some Wire is Broken ";
            break;
        case 3:
            complaint = "Socket in Which the mouse is pluged in is not working";
            break;
        default:
        {
            space(44);
            cout << "Inavlid Input " << endl;
            exit(1);
        }
        }
        file_store(LabNo, system, device, complaint);
        format(30, "! ");
        cout << "YOUR COMPLAINT HAS BEEN SUCCESSFULLY REGISTERED ";
        format(35, " !");
        cout << endl
             << endl;
    }
    break;
    case 2:
    {
        cout << endl;
        format(42, "* ");
        cout << "CPU";
        format(42, "* ");
        cout << endl;
        space(44);
        cout << "Enter System No : ";
        cin >> system;
        // check if the system number is valid or not
        device = "CPU";
        int m;
        cout << endl
             << setw(100) << "SELECT COMPLAINT " << endl;
        cout << setw(61) << "1 : Slow Working " << endl
             << endl
             << setw(68) << "2 : Some Wire is Broken " << endl
             << endl
             << setw(79) << "3 : Sockets in CPU are not working " << endl
             << endl;
        space(44);
        cout << "Enter an appropriate number : " << '\t' << '\t';
        cin >> m;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:
            complaint = "Slow Working";
            break;
        case 2:
            complaint = "Some Wire is Broken ";
            break;
        case 3:
            complaint = "Sockets in CPU are not working";
            break;
        default:
        {
            space(44);
            cout << " !!! Inavlid Input !!!" << endl;
            exit(1);
        }
        }
        file_store(LabNo, system, device, complaint);
        cout << endl;
        space(56);
        cout << " YOUR COMPLAINT HAS BEEN SUCCESSFULLY REGISTERED    " << endl;
    }
    break;
    case 3:
    {
        format(42, "* ");
        cout << "MONITOR";
        format(42, "* ");
        cout << endl
             << endl;
        space(44);
        cout << "Enter System No : " << '\t' << '\t';
        cin >> system;
        // check if the system number is valid or not
        device = "Mointer";
        int m;
        cout << endl
             << setw(100) << "SELECT COMPLAINT " << endl;
        cout << setw(61) << "1 : Slow Working " << endl
             << endl
             << setw(68) << "2 : Some Wire is Broken " << endl
             << endl
             << setw(68) << "3 : Sockets not working " << endl
             << endl
             << setw(63) << "4 : Blurred Screen " << endl
             << endl;
        space(44);
        cout << "Enter an appropriate number : " << '\t' << '\t';
        cin >> m;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:
            complaint = "Slow Working";
            break;
        case 2:
            complaint = "Some Wire is Broken ";
            break;
        case 3:
            complaint = "Sockets not working";
            break;
        case 4:
            complaint = "Blurred Screen ";
            break;
        default:
        {
            space(44);
            cout << " !!! Inavlid Input !!! " << endl;
            exit(1);
        }
        }
        file_store(LabNo, system, device, complaint);
        cout << endl;
        space(56);
        cout << "YOUR COMPLAINT HAS BEEN SUCCESSFULLY REGISTERED " << endl;
    }
    break;
    case 4:
    {
        format(42, "* ");
        cout << "KEYBOARD";
        format(42, "* ");
        cout << endl
             << endl;
        space(44);
        cout << "Enter System No : " << '\t' << '\t';
        cin >> system;
        // check if the system number is valid or not
        device = "Keyboard";
        int m;
        cout << endl
             << setw(100) << "SELECT COMPLAINT " << endl;
        cout << setw(61) << "1 : Slow Working " << endl
             << endl
             << setw(68) << "2 : Some Wire is Broken " << endl
             << endl
             << setw(68) << "3 : Keys are Coming off " << endl
             << endl;
        space(44);
        cout << "Enter an appropriate number : " << '\t' << '\t';
        cin >> m;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:
            complaint = "Slow Working";
            break;
        case 2:
            complaint = "Some Wire is Broken ";
            break;
        case 3:
            complaint = "Keys are Coming off ";
            break;
        default:
        {
            space(44);
            cout << " !!! Inavlid Input !!! " << endl;
            exit(1);
        }
        }
        file_store(LabNo, system, device, complaint);
        cout << endl;
        space(56);
        cout << "YOUR COMPLAINT HAS BEEN SUCCESSFULLY REGISTERED " << endl;
    }
    break;
    case 5:
    {
        cout << setw(100) << "SOME OTHER COMPLAINTS" << endl
             << endl;
        int m;
        cout << endl
             << setw(100) << "SELECT COMPLAINT " << endl;
        cout << setw(63) << "1 : Short Circuit " << endl
             << endl
             << setw(78) << "2 : Switches in Lab Not working " << endl
             << endl
             << setw(68) << "3 : Not enough Chairs  " << endl
             << endl;
        space(44);
        cout << "Enter an appropriate number : " << '\t' << '\t';
        cin >> m;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (m)
        {
        case 1:
            complaint = "Short Circuit ";
            break;
        case 2:
            complaint = "Switches in Lab Not working ";
            break;
        case 3:
            complaint = "Not enough Chairs ";
            break;
        default:
        {
            space(44);
            cout << " !!! Inavlid Input !!! " << endl;
            exit(1);
        }
        }
        general_file_store(LabNo, complaint);
        cout << endl;
        space(56);
        cout << "YOUR COMPLAINT HAS BEEN SUCCESSFULLY DONE " << endl;
    }
    break;
    case 6:
        break;
    default:
        cout << "Invalid Input " << endl;
    }
}

int main()
{
    Student user;
    Admin edit;
    int j = 1;
    while (j != 0)
    {
        if (j == 0)
            break;
        int z;
        box();
        cout << setw(10) << endl
             << setw(248) << "Select login option :" << endl
             << endl
             << endl
             << '\t' << setw(48) << "1. Admin " << endl
             << endl
             << '\t' << setw(49) << "2. Student" << endl
             << endl
             << '\t' << setw(46) << "3. Exit" << endl
             << endl;
        space(47);
        cin >> z;
        cout << endl;
        if (z == 1)
        {
            format(68, "-");
            cout << " YOU HAVE ENTERED THE ADMIN SECTION ";
            format(74, "-");
            edit.setID();
            edit.perform();
        }
        else if (z == 2)
        {
            format(66, "-");
            cout << " YOU HAVE ENTERED THE STUDENT SECTION ";
            format(74, "-");
            cout << endl
                 << endl;
            user.setID();
            user.perform();
        }
        else if (z == 3)
        {
            format(61, "<");
            cout << "   YOU HAVE EXITED FROM THE SYSTEM SUCCESSFULLY   ";
            format(67, ">");
            cout << endl
                 << endl;
            j = 0;
        }
        else
        {
            cout << endl;
            space(50);
            cout << " ! ! !  Invalid choice selected please select again ! ! !" << endl
                 << endl;
        }
        if (z != 3)
        {
            cout << endl;
            format(30, "< ");
            cout << "  Press 1 -  Go back to login section";
            format(40, "> ");
            cout << endl
                 << endl;
            format(31, "< ");
            cout << " Press 2 -  Exit";
            space(21);
            format(39, " >");
            cout << endl
                 << endl;
            space(44);
            try
            {
                cin >> j;
                if (j == 1)
                    j = 1;
                else if (j == 2)
                    j = 0;
                else
                    throw 1;
            }
            catch (int x)
            {
                cout << setw(60) << "invalid input....Exiting" << endl;
                j = 0;
            }
        }
    }
    cout << endl;
    cout << setw(91) << " T H A N K S " << endl;
    return 0;
}
void box()
{
    int column = 178;
    for (int j = 0; j < column; j++)
        cout << "=";
    cout << endl;
    cout << setw(280) << " |  LAB MANAGEMENT SYSTEM  | " << endl
         << endl;
    for (int j = 0; j < column; j++)
        cout << "=";
    cout << endl;
}
void space(int sp)
{
    for (int i = 0; i < sp; i++)
        cout << " ";
}
void format(int f, string s)
{
    for (int j = 0; j < f; j++)
        cout << s;
}
