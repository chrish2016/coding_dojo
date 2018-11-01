import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { UserComponent } from './user/user.component';
import { LandingComponent } from './landing/landing.component';
import { UserdetailComponent } from './userdetail/userdetail.component';
import { UserPublicComponent } from './user/user-public/user-public.component';
import { UserPrivateComponent } from './user/user-private/user-private.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    UserComponent,
    LandingComponent,
    UserdetailComponent,
    UserPublicComponent,
    UserPrivateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
