import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ShortestPathService {

  private apiUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) { }

  findShortestPath(start: any, end: any): Observable<any> {
    const data = { start, end };
    return this.http.post<any>(`${this.apiUrl}/find_shortest_path`, data);
  }
}
