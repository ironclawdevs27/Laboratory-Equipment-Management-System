#include <iostream>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <string>
#include <ios>
#include <limits>

using namespace std;
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

class Login
{
public:
    virtual void setID(void){};
    virtual void perform(void){};
};

class Student : public Login
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
            cout << "Enter system ID of the system you want to see status of :" << endl;
            cin >> system;
            cout << "The status of the system is :" << endl;
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

class Admin : public Login
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
             << "4.Modify" << endl;
        cin >> input;
        switch (input)
        {
        case 1:
            cout << "The system information is :" << endl;
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
            int sys;
            cout << "How many systems would you like to add? :" << endl;
            cin >> sys;
            break;
        case 4:
            cout << "Enter system ID to be replaced :" << endl;
            cin >> replace;
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