"use server"

import { revalidatePath } from "next/cache"
import { Post, User } from "./models"
import { connectToDb } from "./utils"
import { signIn, signOut } from "./auth"
import bcrypt from "bcryptjs"

// use server need to have async function, return value may not be async
export const addPost = async (formData) => {
    // const title = formData.get('title')

    const {title, desc, img, id, userId} = Object.fromEntries(formData)

    try {
        connectToDb()
        const newPost = new Post({
            title,
            desc, 
            id, 
            userId,
            img
        })

        await newPost.save()
        console.log("save to DB");
        revalidatePath('/blog')
    } catch (err) {
        console.log(err);
        return {error: "Error!!!"}
    }

}

export const deletePost = async (formData) => {

    const {id} = Object.fromEntries(formData)

    try {
        connectToDb()
        console.log('id', id);
        await Post.findByIdAndDelete(id)
        console.log("deleted from DB");
        revalidatePath('/blog')
    } catch (err) {
        console.log(err);
        return {error: "Error!!!"}
    }

}

export const handleGithubLogin = async () => {
    "use server"
    await signIn("github")
}

export const handleLogout = async () => {
    "use server"
    await signOut()
}

export const register = async (previousState, formData) => {
    const {username, email, password, passwordRepeat, img} = Object.fromEntries(formData)
    console.log(username, email, password);

    if(password !== passwordRepeat){
        return {error: 'Password do not match'}
        // throw new Error('Password do not match')
    }

    try {
        connectToDb()

        const user = await User.findOne({username})
        if(user){
            return {error: "Username already exists!"}
        }

        const salt = await bcrypt.genSalt(10)
        const hashedPassword = await bcrypt.hash(password, salt)

        const newUser = new User ({
            username,
            email,
            password: hashedPassword,
            img
        })

        await newUser.save()
        console.log('saved to db');

        return {success:true}
    } catch (err) {
        console.log(err);
        return {error:'something went wrong!'}
    }
}

export const login = async (previousState, formData) => {
    const {username, password} = Object.fromEntries(formData)

    try {
        await signIn("credentials", {username, password})
    } catch (err){
        if(err.message.trim().includes("CredentialsSignin")){
            return {error: "Invalid name or password"}
        } 
        // else (err.message.includes("Wrong credentials")) {
        //     return {error: "Something wrong!"}
        // }
        throw err
    }
}

export const addUser = async (prevState,formData) => {
    const { username, email, password, img } = Object.fromEntries(formData);
  
    try {
      connectToDb();
      const newUser = new User({
        username,
        email,
        password,
        img,
      });
  
      await newUser.save();
      console.log("saved to db");
      revalidatePath("/admin");
    } catch (err) {
      console.log(err);
      return { error: "Something went wrong!" };
    }
  };
  
  export const deleteUser = async (formData) => {
    const { id } = Object.fromEntries(formData);
  
    try {
      connectToDb();
  
      await Post.deleteMany({ userId: id });
      await User.findByIdAndDelete(id);
      console.log("deleted from db");
      revalidatePath("/admin");
    } catch (err) {
      console.log(err);
      return { error: "Something went wrong!" };
    }
  };