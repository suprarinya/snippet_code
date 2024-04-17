import { AfterViewInit, Component, ComponentRef, ElementRef, Inject, OnInit, Optional, ViewChild, ViewContainerRef } from '@angular/core';
import { RoomsComponent } from './rooms/rooms.component';
import { LoggerService } from './logger.service';
import { localStorageToken } from './localstorage.token'; 
import { InitService } from './init.service';

@Component({
  selector: 'hinv-root',
  templateUrl: './app.component.html',
  // template: '<h1>Test</h1>',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, AfterViewInit {
  title = 'hotelinventoryapp';

  role = "Admin"
  // static:true => no synchronous/async code => can use fun in ngOnInit
  // static:false => can only access element in ngAfterViewInit
  @ViewChild('name', {static:true}) name!: ElementRef
  // @ViewChild('user', {read: ViewContainerRef}) vcr !: ViewContainerRef

  constructor(@Optional() private loggerservice: LoggerService, 
  @Inject(localStorageToken) private localStorage: Storage,
  private initService: InitService
  ){
    console.log(initService.config);
    
  }

  ngOnInit(): void {
    this.loggerservice?.log('AppComponent.ngOnInit()')
    this.name.nativeElement.innerText = "Marine Hotel"
    console.log(this.name.nativeElement);
    this.localStorage.setItem('name', 'Hilton Hotel')
    
  }

  ngAfterViewInit(): void {
  //   const componentRef = this.vcr.createComponent(RoomsComponent)
  //   componentRef.instance.numberOfRoom = 50;
  }
}
