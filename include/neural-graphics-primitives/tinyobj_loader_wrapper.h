/*
 * Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
 *
 * NVIDIA CORPORATION and its licensors retain all intellectual property
 * and proprietary rights in and to this software, related documentation
 * and any modifications thereto.  Any use, reproduction, disclosure or
 * distribution of this software and related documentation without an express
 * license agreement from NVIDIA CORPORATION is strictly prohibited.
 */

/** @file   tinyobj_loader_wrapper.h
 *  @author Thomas Müller, NVIDIA
 *  @brief  Wrapper around the tinyobj_loader library, providing a simple
 *          interface to load OBJ-based meshes.
 */

#pragma once

#include <neural-graphics-primitives/common.h>

#include <string>
#include <vector>

namespace ngp {

std::vector<vec3> load_obj(const fs::path& path);
Mesh load_obj_complete(const fs::path& path);

}
