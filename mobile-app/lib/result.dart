import 'package:flutter/material.dart';

class MyAbp extends StatelessWidget {
  late String text123;
  MyAbp({Key? key, required String this.text123}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Results")),
      body: Center(
        child: Text(
          text123,
          style: TextStyle(fontSize: 24,color: Colors.black),
        ),
      ),
    );
  }
}

class results extends StatefulWidget {
  const results({Key? key}) : super(key: key);

  @override
  State<results> createState() => _resultsState();
}

class _resultsState extends State<results> {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
