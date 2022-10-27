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
