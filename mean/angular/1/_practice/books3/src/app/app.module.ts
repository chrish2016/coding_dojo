import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // <-- Import FormsModule
import { HttpModule } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import * as fromBooks from './books';
// import * as fromServices from './services';


@NgModule({
  declarations: [
    AppComponent,
    ...fromBooks.components
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule,
    HttpClientModule
  ],
  // providers: [...fromServices.services],
  bootstrap: [AppComponent]
})
export class AppModule { }
