import { NextResponse } from "next/server";
import jwt from 'jsonwebtoken'

const staticFileExtensions = /\.(js|css|png|jpg|jpeg|svg|gif|woff|woff2|ttf|ico)$/;
const publicPath = ['/login', '/register']

export function middleware(req, res) {
  const { pathname } = req.nextUrl;

  if (staticFileExtensions.test(pathname) || publicPath.includes(pathname)) {
    return NextResponse.next();
  }

  
  try {
    const token = req.cookies.get('userdata')
    const tokenString = token.value;
    // const verify = jwt.verify(tokenString, process.env.NEXT_PUBLIC_JWT_SECRET);
    if(tokenString){
      return NextResponse.next();
    } else {
      throw Error('')
    }
    
  } catch (err) {
    // Token verification failed; redirect to login
    console.log('err: ', err);
    const url = `${process.env.NEXT_PUBLIC_NEXT_URI}/login`
    return NextResponse.redirect(url);
  }
}
