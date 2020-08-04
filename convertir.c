#include <stdio.h>
#include <string.h>

int numero;
main()
{  
	  convertir();
}
convertir()
{
     int unidad=0;
     int decena=0;
     int numero=0;
     char Cadena[200];     
     char Auxiliar[200];
     Cadena[0]='\0';


printf("\nNumero : ");
scanf("%d",&numero);
unidad = numero % 10 ;
decena = numero / 10 ;

switch(decena)
{
case 1:
strcpy(Cadena,"diez");
break;
case 2:
strcpy(Cadena,"veinte");
break;
case 3:
strcpy(Cadena,"treinta");
break;
case 4:
strcpy(Cadena,"cuarenta");
break;
case 5:
strcpy(Cadena,"cincuenta");
break;
case 6:
strcpy(Cadena,"sesenta");
break;
case 7:
strcpy(Cadena,"setenta");
break;
case 8:
strcpy(Cadena,"ochenta");
break;
case 9:
strcpy(Cadena,"noventa");
break;
case 10:
strcpy(Cadena,"Cien");
break;

}
// Unidades
// el problema con las unidades ocurre porque no cumplen una
// regla fija hasta el numero treinta y por lo tanto hay que evaluar
// las decenas para saber a que número corresponden
if (decena==0 || decena==2) {
switch(unidad)
{ 
case 0:
strcpy(Cadena,"cero");
break;
case 1:
strcpy(Cadena,"uno");
break;
case 2:
strcpy(Cadena,"dos");
break;
case 3:
strcpy(Cadena,"tres");
break;
case 4:
strcpy(Cadena,"cuatro");
break;
case 5:
strcpy(Cadena,"cinco");
break;
case 6:
strcpy(Cadena,"seis");
break;
case 7:
strcpy(Cadena,"siete");
break;
case 8:
strcpy(Cadena,"ocho");
break;
case 9:
strcpy(Cadena,"nueve");
}
}
if (decena==1) {
switch(unidad)
{ 
case 0:
strcpy(Cadena,"diez");
break;
case 1:
strcpy(Cadena,"once");
break;
case 2:
strcpy(Cadena,"doce");
break;
case 3:
strcpy(Cadena,"trece");
break;
case 4:
strcpy(Cadena,"catorce");
break;
case 5:
strcpy(Cadena,"quince");
break;
case 6:
strcpy(Cadena,"dieciseis");
break;
case 7:
strcpy(Cadena,"diecisiete");
break;
case 8:
strcpy(Cadena,"dieciocho");
break;
case 9:
strcpy(Cadena,"diecinueve");
}
}     
// si se trata de los numeros entre el 20 y 29
if(decena==2) {
  if (unidad==0)
  {
  	strcpy(Cadena,"veinte");
  }	
  else
  {
    strcpy(Auxiliar,"veinti");
    strcat(Auxiliar,Cadena);
    strcpy(Cadena,Auxiliar);
  }
}
// numeros superiores a 29
if(decena>2 && decena<10 && unidad!=0) {
strcat(Cadena," y ");
switch(unidad)
{ 
case 1:
strcat(Cadena,"uno");
break;
case 2:
strcat(Cadena,"dos");
break;
case 3:
strcat(Cadena,"tres");
break;
case 4:
strcat(Cadena,"cuatro");
break;
case 5:
strcat(Cadena,"cinco");
break;
case 6:
strcat(Cadena,"seis");
break;
case 7:
strcat(Cadena,"siete");
break;
case 8:
strcat(Cadena,"ocho");
break;
case 9:
strcat(Cadena,"nueve");
break;
}
}
// Visualizar el resultado
printf("\nEl numero %d es %s\n",numero,Cadena);     
//system("PAUSE");
}