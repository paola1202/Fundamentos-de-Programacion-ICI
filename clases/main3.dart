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