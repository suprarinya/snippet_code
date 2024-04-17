import Image from 'next/image';
import styles from './singlePost.module.css'
import PostUser from '@/components/postUser/postUser';
import { Suspense } from 'react';
import { getPost } from '../../../../lib/data';


// fetch data with an api
const getData = async (id) => {
    const res = await fetch(`http://localhost:3001/api/blog/${id}`)
    if(!res.ok){
        throw new Error("Something went wrong")
    }

    return res.json()
}

// export const generateMetadata = async ({params}) => {
//     const {id} = params
//     const post = await getPost(id)

//     return {
//         title: post.title,
//         description: post.desc,
//     }
// }



const SinglePostPage = async ({params}) => {
    const {id} = params
    // get data with an api
    const post = await getData(id)
    // get data without an api 
    // const post = await getPost(id)


    return (
        <div className={styles.container}>
            { post.img && (
                <div className={styles.imgContainer}>
                    <Image 
                    className={styles.img} 
                    src={post.img} 
                    alt='' 
                    fill />
                </div>
            )}
            <div className={styles.textContainer}>
                <h1 className={styles.title}>{post.title}</h1>

                <div className={styles.detail}>

                    {/* <Image 
                    className={styles.avatar} 
                    src='https://images.unsplash.com/photo-1633332755192-727a05c4013d?q=80&w=1480&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' 
                    alt='' 
                    width={50}
                    height={50}/>
                    <div className={styles.detailText}>
                        <span className={styles.detailTitle}>Author</span>
                        <span className={styles.detailValue}>Terry Jeffer</span>
                    </div> */}
                    {post && (
                        <Suspense fallback={<div>Loading...</div>}>
                            < PostUser userId={post.userId} />
                        </Suspense>
                    )}


                    <div className={styles.detailText}>
                        <span className={styles.detailTitle}>Published</span>
                        <span className={styles.detailValue}>{post.createdAt.toString().slice(0, 10)}</span>
                    </div>
                </div>
                <div className={styles.content}>{post?.desc}</div>
            </div>
        </div>
        
    )
}

export default SinglePostPage;