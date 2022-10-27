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