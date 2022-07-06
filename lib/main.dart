import 'package:flutter/material.dart';
import 'dart:math';
void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.grey,
        appBar: AppBar(centerTitle: true, title: Text('Dice'),backgroundColor: Colors.blueGrey,),
        body: Diceroll(),
      ),
    );
  }
}
class Diceroll extends StatefulWidget {
  @override
  State<Diceroll> createState() => _DicerollState();
}

class _DicerollState extends State<Diceroll> {
  var leftDiceNumber = 1;
  var rightDiceNumber = 6;
  void changeDiceFace(){
    setState(() {
      leftDiceNumber = Random().nextInt(5)+1;});
    setState(() {
      rightDiceNumber = Random().nextInt(5)+1;});
  }
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Row(
        children: [
          Expanded(
              flex: 1,
              child: TextButton(
                onPressed: (){
                 changeDiceFace();
                },
                child: Image(
                  image: AssetImage('images/dice_$leftDiceNumber.jpg'),
                ),
              )),
          Expanded(
              flex: 1,
              child: TextButton(
                onPressed: (){
                 changeDiceFace();
                },
                child: Image(
                  image: AssetImage('images/dice_$rightDiceNumber.jpg'),
                ),
              )),
        ],
      ),
    );
  }
}





