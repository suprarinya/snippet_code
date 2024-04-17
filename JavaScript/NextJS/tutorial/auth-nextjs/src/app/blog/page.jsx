import PostCard from '@/components/postCard/postCard';
import styles from './blog.module.css'
import { getPosts } from '../../../lib/data';

// fetch data with an api
const getData = async () => {
    const res = await fetch("http://localhost:3001/api/blog", {next:{revalidate:3600}})
    // {cache:"force-cache"} => if do not want browser to cache , default or {cache:"no-store"}

    if(!res.ok){
        throw new Error("Something went wrong")
    }

    return res.json()
}

const BlogPage = async () => {

    // fetch data with an api
    const posts = await getData()
    // console.log(posts);

    // fetch data without an api
    // const posts = await getPosts()

    return (
        <div className={styles.container}>
            {posts.map((post) => (
                <div className={styles.post} key={post.id}>
                    <PostCard post={post}/>
                </div>
            ))}
        </div>
    )
}

export default BlogPage;