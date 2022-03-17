#include<iostream>
#include<fstream>
#include<string.h>
#include<conio.h>
#include<cstdio>
#include<stdlib.h>
using namespace std;
struct r{
    char dish[50];
    int key;
    float price;
}r;
class Resturant
{
public:
    void create();
    void query();
    void display();
    void update();
    void delet();
    void admin();
};
void Resturant::create()
{
    char a;
    int k;
    fstream obj;
    top:
    do {
        obj.open("resturant.txt",ios::in|ios::binary);
        cout<<"enter the dish key:";
        cin>>k;
         while(obj.read((char*)&r,sizeof(r)))
            {
                if(r.key==k)
                {
                    cout<<"key is already exist"<<endl;
                    obj.close();
                goto top;
                }
            }
        obj.close();
        obj.open("resturant.txt",ios::app|ios::binary);
        r.key=k;
        cin.ignore();
        cout<<"ENTER THE DISH NAME:";
        gets(r.dish);
        cout<<"ENTER THE DISH PRICE:";
        cin>>r.price;
        obj.write((char*)&r,sizeof(r));
        cout<<"do you want to add an other [y/n]:";
        cin>>a;
        obj.close();
    }
    while(a!='n');
}
void Resturant::display()
{
      int c=0;
     fstream obj;
     obj.open("resturant.txt",ios::in|ios::binary);
    cout<<"\tKey\t\tDISH NAME\t\tPRICE"<<endl;
    while(obj.read((char*)&r,sizeof(r)))
    {
            cout<<"\t"<<r.key<<"\t\t"<<r.dish<<"\t\t\t"<<r.price<<endl;
            c++;
    }
    if(c==0)
    {
        cout<<"list is empty"<<endl;
    }
    obj.close();
}
void Resturant::query()
{
     int a,c=0;
     fstream obj;
     obj.open("resturant.txt",ios::in);
    cout<<"enter the dish key:";
    cin>>a;
    while(obj.read((char*)&r,sizeof(r)))
    {
           if(r.key==a)
           {
            cout<<"\t"<<r.key<<"\t\t"<<r.dish<<"\t\t\t"<<r.price<<endl;
            c++;
           }
    }
    if(c==0)
    {
        cout<<"not found"<<endl;
    }
    obj.close();
}
void Resturant::update()
{
     int a,p,c=0;
     fstream obj;
     obj.open("resturant.txt",ios::in|ios::out|ios::binary);
    cout<<"enter the dish key:";
    cin>>a;
    obj.seekg(0);
    while(obj.read((char*)&r,sizeof(r)))
    {
        if(r.key==a)
        {
            cout<<"destinatio record:"<<endl;
            cout<<"\t"<<r.key<<"\t\t"<<r.dish<<"\t\t\t"<<r.price<<endl;
            p=obj.tellg()-(sizeof(r));
            obj.seekp(p);
            cout<<"enter the dish key:";
            cin>>r.key;
            cin.ignore();
            cout<<"ENTER THE DISH NAME:";
             gets(r.dish);
            cout<<"ENTER THE DISH PRICE:";
            cin>>r.price;
            obj.write((char*)&r,sizeof(r));
            c++;
           }

        }
        if(c==0)
        {
            cout<<"not found"<<endl;
        }

    obj.close();
}
void Resturant::delet()
{
     int a,c;
     fstream obj,obj1;
     obj.open("resturant.txt",ios::in|ios::binary);
     obj1.open("temp.txt",ios::app|ios::binary);
    cout<<"enter the dish key:";
    cin>>a;
    while(obj.read((char*)&r,sizeof(r)))
    {
        if(r.key==a)
        {
            c++;
            cout<<"\t"<<r.key<<"\t\t"<<r.dish<<"\t\t\t"<<r.price<<endl;
            cout<<"destination record is deleted"<<endl;
        }
        if(r.key!=a)
        {
            obj1.write((char*)&r,sizeof(r));
           }
    }
    obj.close();
    obj1.close();
    if(c==0)
       {
         cout<<"not found"<<endl;
       }
    remove("resturant.txt");
    rename("temp.txt","resturant.txt");
}
 void Resturant::admin()
{
char a;
    do{

            cout<<"\n\t\t\t\t\t\t|||||||||||||||||||||||||"<<endl;
            cout<<"\t\t\t\t\t\t|                       |"<<endl;
            cout<<"\t\t\t\t\t\t|  1) ADD DISH          |"<<endl;
            cout<<"\t\t\t\t\t\t|  2) Display           |"<<endl;
            cout<<"\t\t\t\t\t\t|  3) QUERY             |"<<endl;
            cout<<"\t\t\t\t\t\t|  4) UPDATE            |"<<endl;
            cout<<"\t\t\t\t\t\t|  5) DELETE            |"<<endl;
            cout<<"\t\t\t\t\t\t|  0) EXIT TO MAIN MANU |"<<endl;
            cout<<"\t\t\t\t\t\t|                       |"<<endl;
            cout<<"\t\t\t\t\t\t|||||||||||||||||||||||||"<<endl;
            cout<<"\t\t\t\t\t\tselect the key";
            cin>>a;
            switch(a)
            {
            case '0':
                break;
            case '1':
                system("CLS");
               create();
                break;
            case '2':
                system("CLS");
               display();
                break;
            case '3':
                system("CLS");
               query();
                break;
            case '4':
                system("CLS");
               update();
                break;
            case '5':
                system("CLS");
             delet();
                break;
            }
    }
    while(a!='0');
}
struct {
char d[50];
float p,amount;
int qty;
}rd;
class custmer:public Resturant
{
public:
    void bill();
    void showbill();
    void dish_menu();
};
void custmer::bill()
{
     int a,c=0;
     char ch;
     float total=0;
    fstream obj,obj1;
    dish_menu();
    obj1.open("bill.txt",ios::out|ios::binary);
     do{
    obj.open("resturant.txt",ios::in|ios::binary);
    cout<<"enter the dish key:";
    cin>>a;
    while(obj.read((char*)&r,sizeof(r)))
    {
           if(r.key==a)
           {
            c++;
            cout<<"enter the quantity:";
            cin>>rd.qty;
            rd.amount=rd.qty*r.price;
            cout<<"\t"<<r.dish<<"\t\t"<<r.price<<"*"<<rd.qty<<"\t\t"<<rd.amount<<endl;
            strcpy(rd.d,r.dish);
            rd.p=r.price;
            obj1.write((char*)&rd,sizeof(rd));
            total=total+rd.amount;
           }
        }
        if(c==0)
     {
        cout<<"not found"<<endl;
     }

    cout<<"do you want to order more [y/n]";
    cin>>ch;
    obj.close();
     }
     while(ch!='n');
    obj1.close();
    cout<<"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"<<endl;
    cout<<"|||||||||||||||||||||||||||||||||||||||||||||||| BILL  |||||||||||||||||||||||||||||||||||||||||||||||||||||||"<<endl;
     cout<<"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"<<endl;
    showbill();
    cout<<"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"<<endl;
    cout<<"|||\t\t\t\t\t\t\t   TOTAL="<<total<<"\t\t\t\t\t   |||"<<endl;
    cout<<"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"<<endl;
}
 void custmer::showbill(){
    fstream obj;
    obj.open("bill.txt",ios::in|ios::binary);
    cout<<"\tDISH NAME\t\tPRICE\t\tQTY\t\tAMOUNT"<<endl;
    while(obj.read((char*)&rd,sizeof(rd)))
    {

            cout<<"\t"<<rd.d<<"\t\t\t"<<rd.p<<"\t\t"<<rd.qty<<"\t\t"<<rd.amount<<endl;


    }
    obj.close();
 }
 void custmer::dish_menu()
 {
      fstream obj;
     obj.open("resturant.txt",ios::in|ios::binary);
    while(obj.read((char*)&r,sizeof(r)))
    {


            cout<<"\t\t"<<r.key<<") "<<r.dish<<"-------RS  "<<r.price<<endl;
    }
    obj.close();
 }
int main()
{
    char a;
    custmer obj;
    do
    {
        cout<<"\n\t\t\t\t\t\t||||||||||||||||||||"<<endl;
        cout<<"\t\t\t\t\t\t|                  |"<<endl;
        cout<<"\t\t\t\t\t\t|    1)Admin       |"<<endl;
        cout<<"\t\t\t\t\t\t|    2)custmer     |"<<endl;
        cout<<"\t\t\t\t\t\t|    0)Exit        |"<<endl;
        cout<<"\t\t\t\t\t\t|                  |"<<endl;
        cout<<"\t\t\t\t\t\t||||||||||||||||||||"<<endl;
        cout<<"\t\t\t\t\t\tselect the manu";
        cin>>a;
        switch(a)
        {
        case '0':
            break;
        case '1':
             system("CLS");
            obj.admin();
            break;
        case '2':
             system("CLS");
            obj.bill();
            break;
        }
    }
    while(a!='0');

}
