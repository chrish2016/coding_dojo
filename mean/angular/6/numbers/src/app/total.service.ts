import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TotalService {
  staticNumbers: number[] = [1,2,3];
  numbers: number[] = [Math.floor(Math.random() * 10)];
  alphanumbers: number[] = [Math.floor(Math.random() * 10)];
  betanumbers: number[] = [Math.floor(Math.random() * 10)];
  totalnumbers: number[] = [];

  constructor() { }

  retrieveNumbers(): number[] {
    return this.numbers;
  }
  
  retrieveAlphaNumbers(): number[] {
    return this.alphanumbers;
  }
  
  retrieveBetaNumbers(): number[] {
    return this.betanumbers;
  }

  

  addAlphaNumber() {
    this.alphanumbers.push(Math.floor(Math.random() * 10));
  }
  addBetaNumber() {
    this.betanumbers.push(Math.floor(Math.random() * 10));
  }
  TotalNumber(retrieveAlphaNumbers, retrieveBetaNumbers){
    retrieveAlphaNumbers - retrieveBetaNumbers;
  }
}
