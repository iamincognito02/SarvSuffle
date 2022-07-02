import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.black,
          appBar: AppBar(
            title: Center(
              child: Text('SARVSUFFLE', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 35.0),
            )),
            backgroundColor: Colors.purple,
          ), //AppBar
          body: SafeArea(
          child:Center(
          child:Column(
          children: [
              Align(alignment: Alignment.topLeft,
            child: Container(
              color: Colors.black,
              margin:
             EdgeInsets.symmetric(vertical: 5.0, horizontal: 0.0),
              padding:
              EdgeInsets.symmetric(vertical: 15.0),
              child: Row(

                children: [
                  Text(
                    "EMPLOYEE'S INFO  ",
                    style: TextStyle(
                        fontWeight: FontWeight.bold, fontSize: 28.0, color: Colors.white),
                  ),
                  ],
              ),
            )),
          Container(
          color: Colors.grey,
          margin:
          EdgeInsets.symmetric(vertical: 10.0, horizontal: 30.0),
          padding:
          EdgeInsets.symmetric(vertical: 15.0, horizontal: 15.0),
          child: Row(
            children: [
              CircleAvatar(
                radius: 50.0,
                backgroundImage: AssetImage('images/Photo.png'),
              ),
              Text('  Kewal Nisar \n  FLUTTER\n  DEVELOPER',
                  style:
                  TextStyle(fontWeight: FontWeight.bold, fontSize: 20.0)),

            ], ),),

        Container(
          color: Colors.grey,
          margin:
          EdgeInsets.symmetric(horizontal: 30.0),
          padding:
          EdgeInsets.symmetric(vertical: 15.0, horizontal: 15.0),
          child: Row(
            children: [
              Icon(
                Icons.phone_android_outlined,
                size: 28.0,
              ),
              SizedBox(
                width: 25.0,
              ),
              Text(
                '9588471585',
                style: TextStyle(
                    fontWeight: FontWeight.bold, fontSize: 25.0),
              ),
            ],
          ),
        ),
        Container(
           margin:
            EdgeInsets.symmetric(horizontal: 30.0),
            padding:
            EdgeInsets.symmetric(vertical: 20.0, horizontal: 15.0),
            color: Colors.grey,
            child: Row(
              children: [
                Icon(
                  Icons.email_outlined,
                  size: 28.0,
                ),
                SizedBox(
                  width: 25.0,
                ),
                Text(
                  'kewalnisar@gmail.com',
                  style: TextStyle(
                      fontWeight: FontWeight.bold, fontSize: 22.0),
                ),
              ],
            )),
            Container(
              color: Colors.grey,
              margin:
              EdgeInsets.symmetric(horizontal: 30.0),
              padding:
              EdgeInsets.symmetric(vertical: 15.0, horizontal: 15.0),
              child: Row(
                children: [
                  Icon(
                    Icons.location_on_outlined,
                    size: 28.0,
                  ),
                  SizedBox(
                    width: 25.0,
                  ),
                  Text(
                    'E - 002, Gloria Grace \nApartments, Bavdhan,\nPune, 411001.',
                    style: TextStyle(
                        fontWeight: FontWeight.bold, fontSize: 20.0),
                  ),
                ],
              ),
            ),
            Container(
              color: Colors.grey,
              margin:
              EdgeInsets.symmetric(horizontal: 30.0),
              padding:
              EdgeInsets.symmetric(vertical: 15.0, horizontal: 15.0),
              child: Row(
                children: [
                  Icon(
                    Icons.date_range_rounded,
                    size: 28.0,
                  ),
                  SizedBox(
                    width: 25.0,
                  ),
                  Text(
                    'DOB - 17/05/2002',
                    style: TextStyle(
                        fontWeight: FontWeight.bold, fontSize: 20.0),
                  ),
                ],
              ),
            ),
            Container(
              color: Colors.grey,
              margin:
              EdgeInsets.symmetric(horizontal: 30.0),
              padding:
              EdgeInsets.symmetric(vertical: 15.0, horizontal: 15.0),
              child: Row(
                children: [
                  Icon(
                    Icons.bloodtype_sharp,
                    size: 28.0,
                  ),
                  SizedBox(
                    width: 25.0,
                  ),
                  Text(
                    'O -ve',
                    style: TextStyle(
                        fontWeight: FontWeight.bold, fontSize: 25.0),
                  ),
                ],
              ),
            ),
      ]),


      ),

    )),
      debugShowCheckedModeBanner: false,
    );

  }
}

