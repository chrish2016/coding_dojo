import { Component, OnInit } from '@angular/core';
import { TotalService } from '../total.service';

@Component({
  selector: 'app-beta',
  templateUrl: './beta.component.html',
  styleUrls: ['./beta.component.css']
})
export class BetaComponent implements OnInit {
  numbers: number[] = [];
  betanumbers: number[] = [];

  constructor(private _totalService: TotalService) { }

  ngOnInit() {
    this.betanumbers = this._totalService.retrieveBetaNumbers();
  }
  pushBeta(num: number) {
    this._totalService.addBetaNumber();
  }

}
