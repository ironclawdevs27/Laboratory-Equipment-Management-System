//if float is given as input it is considered valid
//exception handling

#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>
#include<ios>
#include<limits>
using namespace std;
void general_file_store(string LabNo, string complaint)
{
    string final;
    final = LabNo + " - " + complaint;
    fstream myfile;
    myfile.open("hello.txt", ios::app);
    myfile << final << endl;
}
void file_store(string LabNo, string system, string device, string complaint)
{
    string final;
    final = LabNo + " " + system + " - " + device + " - " + complaint;
    fstream myfile;
    myfile.open("hello.txt", ios::app);
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
    cin.ignore(numeric_limits<streamsize>::max(),'\n');
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
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
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
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
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
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
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
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
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
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
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
int main()
{
    generic_complaints();
    return 0;
}