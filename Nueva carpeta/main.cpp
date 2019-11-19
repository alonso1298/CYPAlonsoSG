#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int x;
	x=10;
	int y = 20;
	
	printf("Hola mundo de programacion C\n");
	printf("Introduce un numereo entero:");
	scanf("%d",&y);
	
	printf("X vale: %d Y vale: %d \a" ,x,y);
	if(y > 10 ){
		printf("\n%d es mayor que 10",y);
	
	}else{
		printf("\n%d es menos que 10",y);
	}
	printf(" Alogo mas");
	
	printf("\n introduce un valor entero entre 1 y 5:") ;
	scanf("%d",&x);
	switch( x ){
	case 1:
		printf("Hola");
		break;
	case 2:
		printf("Adios");
		break;
	case 3:
		printf("Hello");
		break;
	case 4:
		printf("Bye");
		break;
	case 5:
		printf("Guten Tag");
		break;
	case 6:
		printf("Buongiorno");
		break;
	default:
		printf("Opccion no valida");
		
	}

	
	
	
}
