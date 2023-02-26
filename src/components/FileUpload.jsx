import React, { useState } from 'react';
import FileDownload from './FileDownload';
import DoubleBubble from './DoubleBubble';
import FileInput from './FileInput';

export default function FileUpload() {
	const [selectedFile, setSelectedFile] = useState();
	const [isSelected, setIsSelected] = useState(false);
	const [isSubmitting, setIsSubmitting] = useState(false);

	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsSelected(true);
	};

	const handleSubmission = () => {
		setIsSubmitting(true);
		const formData = new FormData();
		formData.append('file', selectedFile);


		fetch(
			'/upload',
			{
				method: 'POST',
				body: formData,
			}
		)
			.then((response) => response.json())
			.then((result) => {
				console.log('Success:', result);
			})
			.catch((error) => {
				console.error('Error:', error);
			})
			.finally(() => {
				setIsSubmitting(false);
			});
	};

	return (
		<>
			<div>
				<FileInput onChange={changeHandler} />
				{isSelected ? (
					<div>
						<p>File Name: {selectedFile.name}</p>
						<p>File Type: {selectedFile.type}</p>
						<p>Size in Bytes: {selectedFile.size}</p>
						<p>
							Date Last Modified:{' '}
							{selectedFile.lastModifiedDate.toLocaleDateString()}
						</p>
					</div>
				) : (
					<p></p>
				)}
				<div>
					{isSubmitting && <DoubleBubble />}
					<FileDownload onClick={handleSubmission} />
				</div>
			</div>
		</>
	);
}