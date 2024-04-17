import { Inject, Injectable } from '@angular/core';
import { Room, RoomList } from '../rooms';
import { environment } from '../../../environments/environment';
import { APP_SERVICE_CONFIG } from 'src/app/AppConfig/appconfig.service';
import { AppConfig } from 'src/app/AppConfig/appconfig.interface';
import { HttpClient, HttpHeaders, HttpRequest } from '@angular/common/http';
import { Observable, shareReplay } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class RoomsService {
  // Service - purpose -> keep all logic from component
  roomList : RoomList[] = []

  // headers = new HttpHeaders({'token':'123456789'}) 
  getRooms$ = this.http.get<RoomList[]>('/api/rooms', {
    // headers: this.headers,
  }).pipe(
    // cache first request data in case call same api multiple times
    shareReplay(1)
  )

  photoList : [] = []
  

  constructor(@Inject(APP_SERVICE_CONFIG)  private config: AppConfig,
  private http: HttpClient) { 
    console.log(environment.apiEndpoint);
    console.log('Rooms Service initialized...');
    
  }

  getRooms() {
    // return this.roomList
    // return this.http.get<RoomList[]>('/api/rooms')
    return this.http.get<RoomList[]>('/api/rooms')
  }

  addRoom(room: RoomList) {
    return this.http.post<RoomList[]>('api/rooms', room, {
      // headers: this.headers,
    })
  }

  editRoom(room: RoomList){
    var room_id = room.roomNumber
    return this.http.put<RoomList[]>(`api/rooms/${room_id}`, room)
  }

  deleteRoom(room_id: string){
    return this.http.delete<RoomList[]>(`api/rooms/${room_id}`)
  }


  // example http
  getPhotos() {
    const request = new HttpRequest(
      'GET',
      // `${this.config.apiEndpoint}/api/rooms/photos`,
      'https://jsonplaceholder.typicode.com/photos',
    {
      reportProgress : true
    })
    return this.http.request(request)
  }
}


// {
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