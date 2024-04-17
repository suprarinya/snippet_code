import { NextResponse } from "next/server";
import { writeFile } from 'fs/promises'

export async function GET(req, res) {

    return NextResponse.json({ message: "Hello World" }, { status: 200 });
  }

  export async function POST(req, res) {
    const formData = await req.formData()
    const file = formData.get("file")

    if (!file) {
        return NextResponse.json({ error: "No files received." }, { status: 400 });
    }

    const buffer = Buffer.from(await file.arrayBuffer())
    const path = `upload/${file.name}`
    await writeFile(`public/${path}`, buffer)
    console.log(`open ${path} to see the uploaded file`)

    return NextResponse.json({ message: path }, { status: 200 });
  }