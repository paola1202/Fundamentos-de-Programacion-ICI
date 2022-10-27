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