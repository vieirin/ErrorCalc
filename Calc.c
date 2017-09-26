#include <stdio.h>
#include <math.h>

void naozoa(char*);
int  baseestimativa(float, float*);
int  baseerro(float, float*);
 

int  main(){
  float delta_a, delta_b, a, b, estimativa, erro, base=0;
  char  d_m;


  printf ("\nA: ");
  scanf  ("%f", &a);
  getchar();
  printf ("\ndA: ");
  scanf  ("%f", &delta_a);
  getchar();
  printf ("\nB: ");
  scanf  ("%f", &b);
  getchar();
  printf ("\ndB: ");
  scanf  ("%f", &delta_b);
  getchar();
  printf ("Multiplicação ou Divisão? (m/d) ");
  scanf  ("%c", &d_m);

  naozoa(&d_m);

  if(d_m=='m'){
//    calcula a multiplicação
      estimativa = (a*b);
      printf       ("Melhor estimativa: %f ", (estimativa*(pow(10, baseestimativa(estimativa, &base)))));
      printf       ("10^%d\n ", (int)base);
      if (delta_a!=0||delta_b!=0){
        erro      =  estimativa*((delta_a/a)+(delta_b/b));
        printf       ("Erro: %f ", (erro*(pow(10, baseerro(erro, &base)))));
        printf       ("* 10^%d\n", (int)base );
      }
      else{
        printf("Erro = 0\n");
      }
    }
    else{
//    calcula a divisão
      estimativa = (a/b);
      printf       ("Melhor estimativa: %f ", (estimativa*(pow(10, baseestimativa(estimativa, &base)))));
      printf       ("* 10^%d\n", (int)base );
      if (delta_a!=0||delta_b!=0){
        erro      =  estimativa*((delta_a/a)+(delta_b/b));
        printf       ("Erro: %f ", (erro*(pow(10, baseerro(erro, &base)))));
        printf       ("* 10^%d\n", (int)base );
      }
      else{
        printf("Erro = 0\n");
      }
    }



  return(0);
}

void naozoa(char *num){
  //nao deixa digitar diferente de divisão/multiplicação
  if(*num=='m'||*num=='d'){
  }
  else{
    scanf("%c", &*num);
    getchar();
    naozoa(&*num);
  }
 }



 int baseestimativa(float estimativa, float* base){
  int forcado, contador;
  //calcula quantas vezes sao necessarias voltar/avançar a virgula
  forcado=(int)estimativa;
  if (estimativa<1){
    if (forcado>=1){}
    else
    {
      for (contador = 0; forcado<1; contador++)
      {
        estimativa = estimativa*10;
        forcado    = (int)estimativa;
      }
    }
    *base = (-contador);
    printf  ("%f\n",  *base);
    return  (contador);
  } 
  else{
    if (forcado>=1||forcado<=10){
      return(0);
    }
    else
    {
      for (contador = 0; forcado>=0; contador++)
      {
        estimativa = estimativa/10;
        forcado    = (int)estimativa;
      }
    }
    *base=contador;
    return(contador);
  }

 }

int baseerro(float erro, float *base){
  int forcado, contador;
  //calcula quantas vezes sao necessarias voltar/avançar a virgula.
  forcado=(int)erro;
  if (erro==0){
    *base=0;
    return(0);
  }
  if (erro>0&&erro<1){
    if (forcado>=1){
      return(0);
    }
    else{    
      for (contador = 0; forcado<1; contador++)
      {
        erro    = erro*10;
        forcado = (int)erro;
      }
    }
    *base=-contador;
    return(contador);
  }
  else{
    if (forcado>=1||forcado<=10){
      return(0);
    }
    else
    {
      for (contador = 0; forcado>=0; contador++)
      {
        erro    = erro/10;
        forcado = (int)erro;
      }
    }
    *base=contador;
    return(contador);
  }

 }
