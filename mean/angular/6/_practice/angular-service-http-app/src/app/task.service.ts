import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'Rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  task: BehaviorSubject<any[]> = new BehaviorSubject([]);

  constructor(private _http: HttpClient) {
    this.retrieveTask();
  }
  
  retrieveTask(){
    this._http.get('https://1127ef1e66a3e50c15e914ac4a41c1449166fda7.mockapi.io/task').subscribe(
      (task: any[]) => { this.task.next(task);}
    );
  }

  addTask(newTask: any){
    this._http.post('https://1127ef1e66a3e50c15e914ac4a41c1449166fda7.mockapi.io/task', newTask).subscribe(
      (response) => {this.retrieveTask(); }
    );
  }
}
