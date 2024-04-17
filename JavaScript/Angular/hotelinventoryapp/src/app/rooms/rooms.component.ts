import { AfterViewChecked, AfterViewInit, Component, DoCheck, OnDestroy, OnInit, QueryList, SkipSelf, ViewChild, ViewChildren } from '@angular/core';
import { Room, RoomList } from './rooms'
import { HeaderComponent } from '../header/header.component';
import { RoomsService } from './services/rooms.service';
import { Observable, Subject, Subscription, catchError, map, of } from 'rxjs';
import { HttpEventType } from '@angular/common/http';

@Component({
  selector: 'hinv-rooms',
  templateUrl: './rooms.component.html',
  styleUrls: ['./rooms.component.css'],

})
export class RoomsComponent implements OnInit, DoCheck, AfterViewInit, AfterViewChecked, OnDestroy {

  hotelName = 'Hiltom Hotel'

  numberOfRoom = 10

  color = "color: teal"

  hideRooms = true

  selectedRoom !: RoomList

  rooms: Room = {
    totalRooms: 120,
    availableRooms: 10,
    bookedRooms: 5
  }

  title = 'Room List'

  // roomList: RoomList[] = [{
  //   roomNumber: 1,
  //   roomType: "Deluxe Room",
  //   amenities: 'Air Condition, Free WiFi, kitchen and TV',
  //   price: 500,
  //   photos: 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80',
  //   checkinTime: new Date('2023-06-14'),
  //   checkoutTime: new Date('2023-06-16'),
  //   rating: 4.14
  // },
  // {
  //   roomNumber: 2,
  //   roomType: "Deluxe Room EX",
  //   amenities: 'Air Condition, Free WiFi, kitchen, bathroom and TV',
  //   price: 1000,
  //   photos: 'https://images.unsplash.com/photo-1566665797739-1674de7a421a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1074&q=80',
  //   checkinTime: new Date('2023-06-20'),
  //   checkoutTime: new Date('2023-06-22'),
  //   rating: 2.98
  // },
  // {
  //   roomNumber: 3,
  //   roomType: "Private Suite",
  //   amenities: 'Air Condition, Free WiFi, kitchen, bathroom, sofa and TV',
  //   price: 1500,
  //   photos: 'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=80',
  //   checkinTime: new Date('2023-06-18'),
  //   checkoutTime: new Date('2023-06-21'),
  //   rating: 3.5
  // }
  // ]

  roomList: RoomList[] = []


  stream = new Observable(observer => {
    observer.next('user1')
    observer.next('user2')
    observer.next('user3')
    // stream complete
    observer.complete()
    // stream error
    // observer.error('error')

  })

  // static: true => we are sure that there's no sychronous code
  // in it and that it will be ready in Parent's onInit
  // make it static:true so that we can access in ngOnInit
  // static: false (default) => when we are not sure if this has 
  // sync or async code i the component or not, can access component
  // in ngViewAfterInit
  // access only first element
  // @ViewChild(HeaderComponent, {static: true}) headerComponent !: HeaderComponent
  @ViewChild(HeaderComponent) headerComponent!: HeaderComponent
  // access all children elements
  @ViewChildren(HeaderComponent) headerChildComponent!: QueryList<HeaderComponent>

  error: string = ''

  totalByte = 0

  subscription !: Subscription;

  error$ = new Subject<string>()

  getError$ = this.error$.asObservable()

  rooms$ = this.roomService.getRooms$.pipe(
    catchError((err) => {
      // console.log('error from stream', err)
      this.error$.next(err.message)
      return of([])
    })
  )

  roomsCount$ = this.roomService.getRooms$.pipe(
    // modify stream
    map((rooms) => rooms.length )
  )

  // roomService = new RoomsService() // this is a service

  // shouldn't access service diretly from template (html)
  // should access within this file only
  // Dependency injection
  // SkipSelf() - when we are sure that the service will be 
  // available, (e.g., parent) - skip checking
  constructor (@SkipSelf() private roomService: RoomsService) {}

  ngOnInit(): void {    
    this.error$
    this.stream.subscribe((data) => console.log(data))
    this.stream.subscribe({
      next: (value) => console.log(value),
      complete: () => console.log('complete1'),
      error: (err) => console.log(err)

    })

    this.roomService.getPhotos().subscribe((event) => {
      // console.log(event.type, event);
      // sent = 0
      // uploadprogress = 1
      // responseheader = 2
      // downloadprogress = 3
      // response = 4
      // user = 5
      switch(event.type){
        case HttpEventType.Sent:
          console.log('Request has been made');
          break
        case HttpEventType.ResponseHeader:
          console.log('Response success!');
          break
        case HttpEventType.DownloadProgress:
          this.totalByte += event.loaded
          break
        case HttpEventType.Response:
          console.log('Request complete');
          console.log(event.body);
          
          
      } 
    })

    // console.log(this.headerComponent, 'oninit');
    // console.log('rooms component', this.roomService.getRooms());
    // this.roomService.getRooms().subscribe(rooms => {
    this.roomService.getRooms$
    // .subscribe(rooms => {
    //   this.roomList = rooms
      
    // })
    


  }

  ngDoCheck(): void {
    // - called anytime there's an event
    // - shouldn't implement both DoCheck and OnChange together 
    // in one component
   console.log('on change is called');
  }

  // after we initialize all view in OnInit and that
  // it's safe to use other component in this view
  ngAfterViewInit(): void {
    // console.log(this.headerComponent);
    // this.headerComponent.title =  "Rooms View"

    // console.log(this.headerChildComponent.first, this.headerChildComponent.last);
    this.headerChildComponent.forEach((e, i)=> {
      if(this.headerChildComponent.length - 1 == i){
        e.title = 'Last Title'
      }
    })
    
  }

  ngAfterViewChecked(): void {
    // if we want to change prev init variable - no error 
    // raised in production mode (it will always raise error
    // in dev mode)
    this.headerComponent.title =  "Rooms View"
  }

  ngOnDestroy(): void {
    console.log('on destroy');
    this.subscription.unsubscribe()
  }

  toggle() {
    this.hideRooms = !this.hideRooms
    this.title     = "Rooms List"
  }

  addRoom() {
    const room: RoomList = {
      // roomNumber: '4',
      roomType: 'Deluxe Room',
      amenities: 'Toiletries, Coffee Kit, Tissue box, Bathrobes and slippers',
      price: 2000,
      photos: 'https://images.unsplash.com/photo-1591088398332-8a7791972843?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80',
      checkinTime: new Date('12-July-2023'),
      checkoutTime: new Date('14-July-2023'),
      rating: 4.5,
    }
  
    // ngonchange -> can only be applied on component 
    // that has input property

    // if not use ChangeDetectionStrategy.OnPush in rooms-list
    // this.roomList.push(room)

    // if use ChangeDetectionStrategy.OnPush (need to be immutablity=>unable to change
    // and can only return new object)
    // this.roomList = [...this.roomList, room]

    // console.log(this.roomList);

    this.roomService.addRoom(room).subscribe((data) => {
      this.roomList = data
    })
    
  }

  selectRoom(room: RoomList) {
    // console.log(room);
    this.selectedRoom = room
  }


  editRoom() {
    const room: RoomList = {
      roomNumber : "3",
      roomType :"Private Suite","amenities":"Air Conditioner, Free Wi-Fi, TV, Bathroom, Kitchen",
      price : 15500,
      photos : "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
      checkinTime : new Date('2023-06-18'),
      checkoutTime : new Date('2023-06-18'),
      rating : 2.6
    }
    this.roomService.editRoom(room).subscribe((data) => {
      console.log(data);
      this.roomList = data
      
    })
  }


  deleteRoom() {
    var room_id = '3'
    this.roomService.deleteRoom(room_id).subscribe((data) =>{
      this.roomList = data
    })
  }

  // getPhotos() {
  //   this.roomService.getPhotos().subscribe((data) => {
  //     console.log(data); 
  //   })
  // }

}
