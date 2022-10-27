# Fundamentos de programación
## Actividades de clase segunda parcial
### Clase 1
```dart


//operaciones basicas
//void main(List<String> args) {
  //var n1 = 15;
  //var n2 = 7;
  //print("suma: $n1 + $n2 = ${n1 + n2}");
  //print("resta: $n1 - $n2 = ${n1 - n2}");
  //print("multiplicacion: $n1 * $n2 = ${n1 * n2}");
  //print("division: $n1 / $n2 = ${n1 / n2}");
  ///print("division entera: $n1 ~/ $n2 = ${n1 ~/ n2}");
  //print(pow(5,3));
  //print("minimo: min($n1, $n2) = ${min(n1, n2)}");
  //print("maximo: max($n1, $n2) = ${max(n1, n2)}");
  //print("seno: ${sin(45 * pi / 180)}");
  //print("coseno: ${cos(45 * pi / 180)}");
  //print("sqrt: ${sqrt(5)}");
  //print(10.isOdd);
  //print(10.isEven);
//}

//Contador positivo
//void main(List<String> args) {
  //var contador = 0;
  //contador = contador + 1;
  //print(contador);
  //contador++;
  //print(contador);
  //++contador;
  //print(contador);
  //contador += 2;
  //print(contador);
//}
//contador negativo
//void main(List<String> args) {
  //var contador = 0;
  //contador = contador + 1;
  //print(contador);
  //contador++;
  //print(contador);
  //++contador;
  //print(contador);
  //contador += 2;
  //print(contador);
//}

//multiplicacion con contador
//void main(List<String> args) {
  //var contador = 0;
  //contador *2;
  //print(contador);
//} 
//division con contador
//void main(List<String> args) {
  //double contador = 0;
  //contador %=2;
  //print(contador);
//}

//void main(list<String> args) {
  //const consentero = 10;
  //var finalentero;
  //var numero = stdin.readLineSync();
  //finalentero = numero;
  //print(numero);
  //print("el mensaje es : $numero");

  //finalentero = "hola";
  
//}

//tiempo de codificacion
//tiempo de compilacion



//void main(List<String> args) {
  //var cadena = 5;

  //print(cadena is String);
  //print(cadena.runtimeType);
  //var nombre = "alex";
  //var edad = 20;
  //print(nombre  );
  //print("$nombre $edad");
//}


//void main(List<String> args) {
  //sistemas numericos
  //binario
  //print(125.toRadixString(2));
  //print(125.toRadixString(8));
  //print(125.toRadixString(16));
  //var numero = 0xFFFF;
  //print(numero.runtimeType);
//}

 void main(List<String> args) {
  //listas
  var milista = [1,"hola",9.8,true];
  print(milista);
  //agregar elementos a lista
  milista.add(3.1416);
  print(milista);
}
```

### Clase 2
```dart
import 'dart:io';
//calculadora que lea dos numeros del teclado y obtenga suma, resta, multiplicación y
//division, usando funciones y asingnado valores a dos variables

void main() {
  String op = leerDatos("Indica la operación [+,-,*,/]");
  int num1 = int.parse(leerDatos("Dame el primer número"));
  int num2 = int.parse(leerDatos("Dame el segundo número"));
  print("${calculadora(op, num1, num2)}");
}

String leerDatos(String mensaje) {
  print(mensaje);
  String data = (stdin.readLineSync()!);
  return data;
}

String calculadora(String op, int n1, int n2) {
  if (op == "+") {
    return "$n1 + $n2 = ${suma(n1, n2)}";
  } else if (op == "-") {
    return "$n1 - $n2 = ${resta(n1, n2)}";
  } else if (op == "*") {
    return "$n1 * $n2 = ${multi(n1, n2)}";
  } else if (op == "/") {
    return "$n1 / $n2 = ${divi(n1, n2)}";
  } else {
    return "Operación inválida";
  }
}

int suma(int num1, int num2) => num1 + num2;
int resta(int num1, int num2) => num1 - num2;
int multi(int num1, int num2) => num1 * num2;
int divi(int num1, int num2) => num1 ~/ num2;
```

### Clase 3
```dart
// void main(){
//   var usuruario1 = User(); //instancia de la clase user 
//   User usuruario2 = User();
//   usuruario1.edad = 19
//   usuruario2.reporte()
//   var estudiante1 = Estudiante();
//   estudiante1.carrera = "Ingenieria en computacion inteligente";
//   estudiante1.noDcuenta = "20185388"
//   estudiante1.semestre = 3;

// }

// class User {
//   //prodpiedades
//   String? nombre; //con el signo de interrogación se permite que la laviable sea nula
//   int? edad; 
//   //metodos
//   void reporte(){
//     print(nombre);
//     print(edad);
//   }
// }

// class Estudiante{
//   int? semestre;
//   String? noDcuenta;
//   String carrera; 
//   void reporte(){
//     print("Carrera: $carrera");
//     print("No. de cuenta; $noDcuenta");
//     print("Semestre: $semestre")
//   }
// }

//void main(){
//  var usuario1 = User(); //instancia de la clase user 
//  User usuario2 = User();
//  usuario1._edad = 19
//  usuario1._nombre
//  usuario2.reporte()
//
//
//}

//encapsulamiento
//- ocultar los atributos de la clase
//- hacerlos locales
//- el simbolo -

//class User {
//  //prodpiedades
//  String? _nombre; //con el signo de interrogación se permite que la laviable sea nula
//  int? _edad; 
//  //metodos
//  void reporte(){
//    print(_nombre);
//    print(_edad);
//  }
//}

void main(List<String>args){
  User usuario1 = User();
  usuario1.nombre = "Paola";
  usuario1.reporte();
}

class User{
    String? _nombre;
    int? _edad; 

    void set nombre(String nombre){
      _nombre = nombre;
    }
    void reporte(){
       print(_nombre);
       print(_edad);
    }
  }
```

### Clase 4
```dart
// una canculadora que sume, reste y multiplique dos numeros como argumentos

/*void main(List<String>args){
 // //invocar
 // print(suma(2,2));
 // //asignacion
 // var res = suma(1,1);
 // print(res);
  Calculadora micalculadora = Calculadora();
  int n1, n2;
  n1 = 5;
  n2 = 8;
  int res = micalculadora.suma(n1.n2);
  print("$n1 + $n2 = $res");

  print("$n1 + $n2 = ${micualculadora.suma(n1,n2)}");
  print("$n1 - $n2 = ${micualculadora.resta(n1,n2)}");
  print("$n1 * $n2 = ${micualculadora.multiplicacion(n1,n2)}");
  print("$n1 / $n2 = ${micualculadora.division(n1,n2)}");
}
*/
/*void main(){ //accediendo a la calculadora con a y b como propiedades 
  Calculadora micalculadora = Calculadora();
  micalculadora.a = 8;
  micalculadora.b = 7;

  int res = micalculadora.suma(micalculadora.a,micalculadora.b);
  print("${micalculadora.a} + ${micalculadora.b} = $res");
}
*/
/**
 * comentarios de documentacion
 * en formato bloque
 */
///comentarios de documentacion en formato linea
void main(args){
  
  int? n1;
  int?  n2;
  if (args.length<1){
    n1 = int.parse(args[0]);
    n2 = int.parse(args[1]);
  }
  else{
    n1 = 5;
    n2 = 8;
  }
  print(n1+n2);
}

//int suma(List<String>args){
//  var sumares = a+b;
//  return sumares; //imperativa 
//}

class Calculadora{
  int a=0;
  int b=0; //porpiedades de la clase 
//declarativa
  int resta(int a, int b)=> a-b;
  int suma(int a, int b)=> a+b; 
  int mul(int a, int b)=> a*b; 
  double division(int a, int b)=> a/b; 
}
```

### Clase 5
```dart
void main(){
 var vehiculo = Vehiculo;
  vehiculo.marca = "Toyota";
  vehiculo.modelo = "Corolla";
  vehiculo.color = 'Blanco';
  vehiculo.llantas = 4;

}

void showVehiculo(){
   
  print("Marca: ${Vehiculo.marca}");
  print("Modelo: ${Vehiculo.modelo}");
  print("Color: ${Vehiculo.color}");
  print("Llantas: ${Vehiculo.llantas}");
}

class Vehiculo{
  int _llantas;
  String _color;
  String _modelo;
  String _marca;

  void set llantas(int llantas) => _llantas = llantas;
  void set color(String color) => _color = color;
  void set modelo(String modelo) => _modelo = modelo;
  void set marca(String marca) => _marca = marca;

  String get color => _color;
  String get marca => _marca;
  String get modelo => _modelo;
  int get llantas => _llantas;

  // Vehiculo (int llantas, String color, String modelo, String marca){
  //  this._llantas = llantas;
  //  this._color = color;
  //  this._modelo = modelo;
  //  this._marca = marca;
  // }

  Vehiculo(this._llantas, this._color, this._modelo, this._marca);
  Vehiculo.marca(this._marca);

  void arrancar(){
    print("El vehiculo esta arrancando");
  }
  void correr(){
    print("El vehiculo esta corriendo");
  }
  void frenar(){
    print("El vehiculo esta frenando");
  }
}
```

### Clase 6
```dart
void main(){
  Perro firulais = new Perro();
  firulais.ladrar();
  firulais._especie = "canino";
  firulais._raza = "salchicha";
  firulais._nombre = "firulais";
  mascota();
  
}

void mascota(){
  Perro firulais = new Perro();
  print("Nombre: ${firulais._nombre}");
}

class Animal{
  String? _especie;
  String? _tipo;
  String? _nombre;

  void caminar(){
    print("Cmaninando");
  }
}

class Perro extends Animal{
  String? _raza;

  void ladrar(){
    print("ladrando");
  }
}

class Ave extends Animal{
  String? _color;

  void volar(){
    print("Volando");
  }
}
```
