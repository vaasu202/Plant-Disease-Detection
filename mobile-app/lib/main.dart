import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:typed_data';
import 'package:http/http.dart' as http;
import 'package:potato_tomato/result.dart';



void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      debugShowCheckedModeBanner: false,
      home: const MyHomePage(title: 'Upload'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}


class _MyHomePageState extends State<MyHomePage> {
  late File _image;
  Uint8List? _imagebytes;

  final picker = ImagePicker();
  
  //Funtion to get the image from the user from the camera only. Gallery option is not given on purpose. The person using the code can enable it.
  void _getimage() async{
    final pickedfile = await picker.getImage(source: ImageSource.camera);
    setState(() {
      if (pickedfile != null){
        _image = File(pickedfile.path);
        _imagebytes = _image.readAsBytesSync();
      }
      else{
        print("No image selected");
      }
    });
  }
  
  //Function to upload the image to the google cloud server(the link given below which passes the image as an argument to the cloud function) and get a response.
  //Function also receives the response and navigates towards a new screen if and only if there is some valid response from the server.
  _uploadfile(File file) async{
    var request = http.MultipartRequest('POST', Uri.parse("https://asia-south1-cryptic-gate-366707.cloudfunctions.net/predict"));
    request.files.add(await http.MultipartFile.fromPath("file",file.path));
    var res = await request.send();
    final respStr = await res.stream.bytesToString();
    print(respStr);
    if (respStr != null){
      setState(() {
        Navigator.pushReplacement(
            context,
            new MaterialPageRoute(
                builder: (BuildContext context) => MyAbp(text123:respStr)));
      });
    }

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(child: _imagebytes == null ? Text("no image selected")
      : Stack(children: [
        Image.memory(_imagebytes!),
        Align(
          alignment: Alignment.bottomCenter,
          child: InkWell(onTap:() => _uploadfile(_image), child: Icon(
              Icons.upload,
              size: 50,
            ),
          ),
        )
      ],)),
      floatingActionButton: FloatingActionButton(
        onPressed: _getimage,
        tooltip: 'Select Image',
        child: const Icon(Icons.add_a_photo),
      ),
    );
  }
}
