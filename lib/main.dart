import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.blueGrey.shade400,
        body: SafeArea(
          child:Center(
           child:Column(
            children: [
              CircleAvatar(
                radius: 50.0,
                
              ),
              Text('Aditya Dimble',
                  style:
                      TextStyle(fontWeight: FontWeight.bold, fontSize: 35.0)),
              Text('FLUTTER DEVELOPER',
                  style:
                      TextStyle(fontSize: 30.0, fontWeight: FontWeight.normal)),
              Container(
                color: Colors.white,
                margin: EdgeInsets.symmetric(vertical: 20.0,horizontal: 30.0),
                padding: EdgeInsets.symmetric(vertical: 15.0,horizontal: 15.0),
                child: Row(
                  children: [
                    Icon(
                      Icons.phone,
                      size: 20.0,
                    ),
                    SizedBox(
                      width: 25.0,
                    ),
                    Text(
                      '9371304202',
                      style: TextStyle(fontSize: 20.0),
                    ),
                  ],
                ),
              ),
              Container(
                  margin: EdgeInsets.symmetric(vertical: 15.0,horizontal: 30.0),
                  padding: EdgeInsets.symmetric(vertical: 15.0,horizontal: 15.0),
                color: Colors.white,

                  child: Row(
                    children: [
                      Icon(
                        Icons.email,
                        size: 20.0,
                      ),
                      SizedBox(
                        width: 25.0,
                      ),
                      Text(
                        'Adidimble1997@gmail.com',
                        style: TextStyle(fontSize: 20.0),
                      ),
                    ],
                  )),

            ],
          ),
        ),
        ),
      ),
    );
  }
}
